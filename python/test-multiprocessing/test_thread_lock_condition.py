#   https://leetcode.com/problems/print-in-order


#   https://leetcode.com/problems/print-in-order/discuss/333424/Python3-threading-and-bitwise-check-solution


from typing import Callable
from threading import Condition
from threading import Thread


def _printFirst():
    print('first')

def _printSecond():
    print('second')

def _printThird():
    print('third')


class Foo:
    def __init__(self):
        self._p = 0
        self._cv = Condition()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        with self._cv:
            printFirst()
            self._p ^= 1
            self._cv.notify_all()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self._cv:
            self._cv.wait_for(lambda: self._p & 1 == 1)
            printSecond()
            self._p ^= 2
            self._cv.notify_all()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self._cv:
            self._cv.wait_for(lambda: self._p & 2 == 2)
            printThird()


def threadExecutor(fooInstance, num):
    if 1 == num:
        fooInstance.first(_printFirst)
    elif 2 == num:
        fooInstance.second(_printSecond)
    elif 3 == num:
        fooInstance.third(_printThird)


f = Foo()
threads = []
for i in [3, 2, 1]:
    threads.append(Thread(target=threadExecutor, args=(f, i)))
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
