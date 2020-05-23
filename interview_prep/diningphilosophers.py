import logging
import threading
from typing import Any

log = logging.getLogger(__name__)
"""
The same instance of Foo will be passed to three different threads.
Thread A will call first(), thread B will call second(), and thread C will call third().
Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().
"""


def print_in_order() -> None:
    order = OrderOrder()
    a = threading.Thread(target=order.first(), args=(1,))
    b = threading.Thread(target=order.second(), args=(2,))
    c = threading.Thread(target=order.third(), args=(3,))
    a.start()
    b.start()
    c.start()

class DiningPhilosophers:

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
