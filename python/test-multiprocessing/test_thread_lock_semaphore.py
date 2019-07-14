#   https://leetcode.com/problems/print-in-order


#   https://leetcode.com/problems/print-in-order/discuss/333562/Python-3-Semaphore


from threading import Semaphore
from threading import Thread


def _printFirst():
    print('first')

def _printSecond():
    print('second')

def _printThird():
    print('third')


class Foo:
    def __init__(self):
        self.two = Semaphore(0)
        self.three = Semaphore(0)

    def first(self, printFirst):
        printFirst()
        self.two.release()

    def second(self, printSecond):
        with self.two:
            printSecond()
            self.three.release()

    def third(self, printThird):
        with self.three:
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
