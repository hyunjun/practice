#   http://hamait.tistory.com/834
from test_eventloop_with_coroutine import EventLoop
from test_eventloop_with_coroutine import print_every
import sys


def fib(n):
    if n <= 1:
        yield n
    else:
        a = yield fib(n - 1)
        b = yield fib(n - 2)
        yield a + b


def read_input(loop):
    while True:
        line = yield sys.stdin
        n = int(line)
        fib_n = yield fib(n)
        print('fib({}) = {}'.format(n, fib(n)))


#   parallel하게 실행 가능
def main():
    loop = EventLoop()
    hello_task = print_every('Hello world!', 3)
    fib_task = read_input(loop)
    loop.schedule(hello_task)
    loop.schedule(fib_task)
    loop.run_forever()


if __name__ == '__main__':
    main()
