from typing import List
import logging

log = logging.getLogger(__name__)


def remove_duplicates_1(nums: List[int]) -> int:
    index = 0
    while index < len(nums) - 1 and len(nums) > 1:
        log.debug(index)
        if nums[index] == nums[index + 1]:
            nums.pop(index)
            index = index - 1 if index > 0 else 0
            continue
        index += 1
    log.debug(nums)
    return nums

def remove_duplicates(nums: List[int]) -> int:
    i = 0
    if len(nums) == 1: return 1
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            i += 1
        nums[i] = nums[j]
        log.debug(nums)
    log.debug("{}, i:{} j:{}".format(nums, i, j))
    if i == 0:
        for k in range(j):
            nums.pop(j - k)
    else:
        for k in range(i + 1):
            nums.pop(j - k)
            log.debug(nums)
    return nums
