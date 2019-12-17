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


#   https://leetcode.com/problems/fizz-buzz-multithreaded/discuss/448726/Python-3-using-one-Barrier
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n

        self.k = 0
        self.div_3 = None
        self.div_5 = None

        def step():
            self.k += 1
            self.div_3 = not self.k % 3
            self.div_5 = not self.k % 5

        self.sync = threading.Barrier(4, action=step)

    def _thread(self, printer, div_3=False, div_5=False):
        while self.k < self.n:
            self.sync.wait()
            if self.div_3 == div_3 and self.div_5 == div_5:
                printer()

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        self._thread(printFizz, div_3=True)

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        self._thread(printBuzz, div_5=True)

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        self._thread(printFizzBuzz, div_3=True, div_5=True)

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        self._thread(lambda: printNumber(self.k))


f, threads = FizzBuzz(15), []
threads.append(threading.Thread(target=f.fizz, args=(printFizz,)))
threads.append(threading.Thread(target=f.buzz, args=(printBuzz,)))
threads.append(threading.Thread(target=f.fizzbuzz, args=(printFizzBuzz,)))
threads.append(threading.Thread(target=f.number, args=(printNumber,)))
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
