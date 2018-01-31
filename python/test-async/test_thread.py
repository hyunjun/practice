#   http://hamait.tistory.com/834
from threading import Thread
from time import sleep
from time import time
from fib import timed_fib


def print_hello():
    while True:
        print('{} - Hello world!'.format(int(time())))
        sleep(3)


def read_and_process_input():
    while True:
        n = int(input())
        print('fib({}) = {}'.format(n, timed_fib(n)))


def main():
    t = Thread(target=print_hello)
    t.daemon = True
    t.start()
    read_and_process_input()


if __name__ == '__main__':
    main()
