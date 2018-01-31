#   http://hamait.tistory.com/834
from bisect import insort
from collections import namedtuple
from fib import timed_fib
from time import time
import selectors
import sys


Timer = namedtuple('Timer', ['timestamp', 'handler'])


class EventLoop:
    def __init__(self, *tasks):
        self._running = False
        self._stdin_handlers = []
        self._timers = []
        self._selector = selectors.DefaultSelector()
        self._selector.register(sys.stdin, selectors.EVENT_READ)

    def run_forever(self):
        self._running = True
        while self._running:
            for key, mask in self._selector.select(0):
                line = key.fileobj.readline().strip()
                for callback in self._stdin_handlers:
                    callback(line)

            while self._timers and self._timers[0].timestamp < time():
                handler = self._timers[0].handler
                del self._timers[0]
                handler()

    def add_stdin_handler(self, callback):
        self._stdin_handlers.append(callback)

    def add_timer(self, wait_time, callback):
        timer = Timer(timestamp=time() + wait_time, handler=callback)
        insort(self._timers, timer)

    def stop(self):
        self._running = False


def main():
    loop = EventLoop()

    def on_stdin_input(line):
        if line == 'exit':
            loop.stop()
            return
        n = int(line)
        print('fib({}) = {}'.format(n, timed_fib(n)))

    def print_hello():
        print('{} - Hello world!'.format(int(time())))
        loop.add_timer(3, print_hello)

    def f(x):
        def g():
            print(x)
        return g

    loop.add_stdin_handler(on_stdin_input)
    loop.add_timer(0, print_hello)
    loop.run_forever()


if __name__ == '__main__':
    main()
