from threading import Lock
from threading import Thread


def printFizz():
    print('fizz')

def printBuzz():
    print('buzz')

def printFizzBuzz():
    print('fizzbuzz')

def printNumber(num):
    print(num)

class FizzBuzz(object):
    def __init__(self, n):
        self.n = n
        self.lock_buzz = Lock()
        self.lock_fizz = Lock()
        self.lock_fizzbuzz = Lock()
        self.lock_num = Lock()
        self.lock_buzz.acquire()
        self.lock_fizz.acquire()
        self.lock_fizzbuzz.acquire()
        # self.lock_num.acquire()


    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        """
        :type printFizz: method
        :rtype: void
        """
        for i in range(3, self.n + 1, 3):
            if i % 15:
                self.lock_fizz.acquire()
                printFizz()
                self.lock_num.release()
        self.lock_fizz.release()


    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz):
        """
        :type printBuzz: method
        :rtype: void
        """
        for i in range(5, self.n + 1, 5):
            if i % 15:
                self.lock_buzz.acquire()
                printBuzz()
                self.lock_num.release()
        self.lock_buzz.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz):
        """
        :type printFizzBuzz: method
        :rtype: void
        """
        for i in range(15, self.n + 1, 15):
            self.lock_fizzbuzz.acquire()
            printFizzBuzz()
            self.lock_num.release()
        self.lock_fizzbuzz.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n + 1):
            self.lock_num.acquire()
            if i % 3 == 0 and i % 5 == 0:
                self.lock_fizzbuzz.release()
            elif i % 3 == 0:
                self.lock_fizz.release()
            elif (i) % 5 == 0:
                self.lock_buzz.release()
            else:
                printNumber(i)
                self.lock_num.release()


f, threads = FizzBuzz(15), []
threads.append(Thread(target=f.fizz, args=(printFizz,)))
threads.append(Thread(target=f.buzz, args=(printBuzz,)))
threads.append(Thread(target=f.fizzbuzz, args=(printFizzBuzz,)))
threads.append(Thread(target=f.number, args=(printNumber,)))
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
