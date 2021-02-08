#   https://leetcode.com/problems/fizz-buzz-multithreaded


import threading


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
        self.cur = 1
        self.sem = threading.Semaphore(1)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        """
        :type printFizz: method
        :rtype: void
        """
        while True:
            self.sem.acquire()
            if self.cur <= self.n and self.cur % 3 == 0 and self.cur % 5 != 0:
                printFizz()
                self.cur += 1
            self.sem.release()

            if self.cur > self.n:
                break


    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz):
        """
        :type printBuzz: method
        :rtype: void
        """
        while True:
            self.sem.acquire()
            if self.cur <= self.n and self.cur % 5 == 0 and self.cur % 3 != 0:
                printBuzz()
                self.cur += 1
            self.sem.release()

            if self.cur > self.n:
                break


    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz):
        """
        :type printFizzBuzz: method
        :rtype: void
        """
        while True:
            self.sem.acquire()
            if self.cur <= self.n and self.cur % 3 == 0 and self.cur % 5 == 0:
                printFizzBuzz()
                self.cur += 1
            self.sem.release()

            if self.cur > self.n:
                break


    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        while True:
            self.sem.acquire()
            if self.cur <= self.n and self.cur % 3 != 0 and self.cur % 5 != 0:
                printNumber(self.cur)
                self.cur += 1
            self.sem.release()

            if self.cur > self.n:
                break


f, threads = FizzBuzz(15), []
threads.append(threading.Thread(target=f.fizz, args=(printFizz,)))
threads.append(threading.Thread(target=f.buzz, args=(printBuzz,)))
threads.append(threading.Thread(target=f.fizzbuzz, args=(printFizzBuzz,)))
threads.append(threading.Thread(target=f.number, args=(printNumber,)))
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
