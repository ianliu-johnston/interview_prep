"""
Contains Helper functions && somethings that are global objects
"""
import logging
import json
import os
import pickle
import sys
import tempfile
import time

from linkedin.deployment.client import rain_client_instance

rain_client = rain_client_instance(name='prod')

# TERMINAL COLORS
RED = "\033[0;31m"
GRN = "\033[0;32m"
CYN = "\033[0;36m"
CLR = "\033[0;00m"

TIMENOW = int(time.mktime(time.localtime()))

CACHE_AND_LOG_NAME = os.path.basename(sys.argv[0])
logging.basicConfig()
log = logging.getLogger(CACHE_AND_LOG_NAME)
log.setLevel(logging.INFO)

DEFAULT_CACHE_TTL = 48000


def set_log_level_debug():
    log.setLevel(logging.DEBUG)


class DiskCache(object):
    """
    sets up memoization with the option to cache to disk with json format
    or as a python byte array with the pickle module
    """
    temp_folder = tempfile.gettempdir()
    CACHEPATH = os.path.join(temp_folder, CACHE_AND_LOG_NAME)
    CACHENAMEFMT = "{name}"

    def __init__(self, name, ttl=DEFAULT_CACHE_TTL, raw_result=None, rw_format='json'):
        self.path = self.CACHEPATH
        self.file_name = self.CACHENAMEFMT.format(name=name)
        self.file_path = os.path.join(self.path, self.file_name)
        self.ttl = ttl
        self.rw_format = rw_format
        try:
            os.makedirs(self.path, exist_ok=True)
        except FileExistsError as err:
            log.debug(err)
            pass

    def set_rw_format(self, rw_format):
        old_rw_format = self.rw_format
        self.rw_format = rw_format
        return(old_rw_format)

    def set_file_name(self, name="cache"):
        """
        :param name: name of the cache
        :param source: name of the cache source
        :return: path of the previous cache file
        """
        old_file_name = self.file_name
        self.file_name = self.CACHENAMEFMT.format(name=name)
        self.file_path = os.path.join(self.path, self.file_name)
        return(old_file_name)

    def write(self, raw_result):
        """
        writes to disk cache file.
        :param raw_result: json object will dump as a string to the disk cache file
        :return: passes the json object through
        """
        if self.rw_format == 'json':
            with open(self.file_path, 'w+') as f:
                json.dump(raw_result, f)
        if self.rw_format == 'pickled':
            with open(self.file_path, 'wb+') as f:
                pickle.dump(raw_result, f)
        return(raw_result)

    def read(self):
        log.debug("{}Reading cache at {} {}".format(CYN, self.file_path, CLR))
        try:
            if TIMENOW - os.path.getmtime(self.file_path) >= self.ttl:
                log.debug("{}Cache has exceeded the TTL of {}s.{}".format(GRN, self.ttl, CLR))
                return None
        except FileNotFoundError:
            log.debug("{}Cache not found.{}".format(GRN, CLR))
            return None
        if self.rw_format == 'json':
            with open(self.file_path, 'r') as f:
                cached_result = json.load(f)
        if self.rw_format == 'pickled':
            with open(self.file_path, 'rb') as f:
                cached_result = pickle.load(f)
        return(cached_result)

    def clear(self):
        log.info("Deleting all cache files except blacklists")
        for _file in os.listdir(self.path):
            if "blacklist" not in _file:
                try:
                    os.remove(os.path.join(self.path, _file))
                except FileNotFoundError:
                    log.error("{} File not found".format(_file))

    def clear_single_cache_file(self, _file):
        log.debug("Removing cache file at: {}".format(os.path.join(self.path, _file)))
        try:
            os.remove(os.path.join(self.path, _file))
        except FileNotFoundError:
            log.error("{} File not found".format(_file))


def memoize(disk_cache, rw_format):
    """
    reads a json blob from a disk cache in /tmp if found,
    else calls the function and writes the result to the disk cache
    :param cache_name: filename
    :param func: function that returns a json object
    :param args: arguments that will be passed to the function
    :param clear: clear the cache or not
    :return: json object
    """
    def wrapper(func):
        def helper(*args, **kwargs):
            old_rw_format = disk_cache.set_rw_format(rw_format)
            cached = disk_cache.read()
            if cached is None:
                cached = func(*args, *kwargs)
                disk_cache.write(cached)
            disk_cache.set_rw_format(old_rw_format)
            return cached
        return helper
    return wrapper
