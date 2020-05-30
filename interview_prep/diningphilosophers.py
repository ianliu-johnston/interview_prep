# import local
from differentfizzbuzz import fizzbuzz_nomod, fizzbuzz_mod

# import from std library
import asyncio
import logging
import random
import threading
from timeit import timeit
from typing import Any

log = logging.getLogger(__name__)


class DiningPhilosophers:
    """
    Demonstrates concurrent programming && resolving deadlock
    """
    def __init__(self, _id=0, name="Nobody", state="ready", left_mutex=None, right_mutex=None):
        self._id = _id
        self.name = name
        self.state = state
        self.left_mutex = left_mutex
        self.right_mutex = right_mutex
        self.thoughts = []

    def wants_to_eat(self):
        with self.left_mutex:
            with self.right_mutex:
                self.eat()
        self.think()

    def eat(self, message=""):
        """
        push thoughts into database
        """
        mod = 0
        nomod = 0
        for thought in self.thoughts:
            if thought['no_mod'] > nomod:
                nomod = thought['no_mod']
            if thought['with_mod'] > mod:
                mod = thought['with_mod']
        print("{} then replied: fizzbuzz with the modulo is {}, whereas without the modulo is {}, therefore, with{} the modulo is faster".\
                format(self.name, mod, nomod, "" if mod >= nomod else "out"))
        self.thoughts.clear()

    def think(self):
        """
        do some sort of analysis
        """
        rand_int = random.randint(1, 3)
        timed_nomod = timeit(fizzbuzz_nomod, number=rand_int)
        timed_mod = timeit(fizzbuzz_mod, number=rand_int)
        self.thoughts.append({"no_mod": timed_nomod, "with_mod": timed_mod})


if __name__ == "__main__":
    philosophers = []
    mutexes = []
    names = ["Descartes", "Neitzsche", "Jung", "Plato", "Russell", "Sartre", "Voltaire"]

    for index, name in enumerate(names)
        philosophers.append(DiningPhilosophers(_id=i, name=name, left_mutex=mutexes[i], right_mutex=[i+1]))
    philosophers.append(DiningPhilosophers(_id=5, name=names[5], left_mutex=mutexes[5], right_mutex=[0]))

    for philosopher in philosophers:
        dining_philosopher = threading.Thread(target=philosopher.wants_to_eat())
        dining_philosopher.start()

