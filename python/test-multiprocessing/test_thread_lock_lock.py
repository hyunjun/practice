#   https://leetcode.com/problems/print-in-order


from typing import Callable
from threading import Lock
from threading import Thread
from time import sleep


def _printFirst():
    print('first')

def _printSecond():
    print('second')

def _printThird():
    print('third')


class Foo:
    counter = 0

    def __init__(self):
        self.lock = Lock()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        while True:
            self.lock.acquire()
            try:
                if 0 == Foo.counter:
                    Foo.counter += 1
                    # printFirst() outputs "first". Do not change or remove this line.
                    printFirst()
                elif 0 < Foo.counter:
                    break
            finally:
                self.lock.release()
            sleep(0.1)


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while True:
            self.lock.acquire()
            try:
                if 1 == Foo.counter:
                    Foo.counter += 1
                    # printSecond() outputs "second". Do not change or remove this line.
                    printSecond()
                elif 1 < Foo.counter:
                    break
            finally:
                self.lock.release()
            sleep(0.1)


    def third(self, printThird: 'Callable[[], None]') -> None:
        while True:
            self.lock.acquire()
            try:
                if 2 == Foo.counter:
                    Foo.counter += 1
                    # printThird() outputs "third". Do not change or remove this line.
                    printThird()
                elif 2 < Foo.counter:
                    break
            finally:
                self.lock.release()
            sleep(0.1)



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
