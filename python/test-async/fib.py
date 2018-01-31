from log_execution_time import log_execution_time


def fib(n):
    return fib(n - 1) + fib(n - 2) if n > 1 else n


timed_fib = log_execution_time(fib)
