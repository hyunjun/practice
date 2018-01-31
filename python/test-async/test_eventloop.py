#   http://hamait.tistory.com/834
import selectors
import sys
from time import time
from fib import timed_fib


def process_input(stream):
    text = stream.readline()
    n = int(text.strip())
    print('fib({}) = {}'.format(n, timed_fib(n)))


def print_hello():
    print('{} - Hello world!'.format(int(time())))


def main():
    selector = selectors.DefaultSelector()
    selector.register(sys.stdin, selectors.EVENT_READ)
    last_hello = 0
    #   Node.js처럼 single thread로 동작
    #   즉 fibonacci 계산을 하는 동안 hello world를 출력하지 않음
    while True:
        for event, mask in selector.select(0.1):
            process_input(event.fileobj)
        if time() - last_hello > 3:
            last_hello = time()
            print_hello()


if __name__ == '__main__':
    main()
