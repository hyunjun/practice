#   https://leetcode.com/problems/print-in-order


#   https://leetcode.com/problems/print-in-order/discuss/333861/Two-Logic-in-Python-with-Comments


from threading import Event
from threading import Thread


def _printFirst():
    print('first')

def _printSecond():
    print('second')

def _printThird():
    print('third')


class Foo(object):
    def __init__(self):
        self.first_done = Event()
        self.second_done = Event()

    def first(self, printFirst):
        printFirst()
        self.first_done.set()

    def second(self, printSecond):
        self.first_done.wait()
        printSecond()
        self.second_done.set()
        self.first_done.clear()
            
    def third(self, printThird):
        self.second_done.wait()
        printThird()
        self.second_done.clear()

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
