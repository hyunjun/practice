from functools import wraps
from time import sleep, time


def time_it(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        return result, end - start
    return wrapper


@time_it
def fast(x):
    return x + 1

@time_it
def slow(x):
    sleep(0.1)
    return x + 1

@time_it
def slow2(x):
    sleep(0.1)
    return x + 2


x0, time0 = fast(1)
x1, time1 = slow(x0)
x2, time2 = slow(x1)


total_time = time0 + time1 + time2


def bind(value_and_time, f):
    result, t = f(value_and_time[0])
    return result, t + value_and_time[1]


x2, t = bind(bind(fast(1), slow), slow2)


#   Monad
#   https://www.youtube.com/watch?v=26jVysJHB-s
class TimedValue:
    def __init__(self, value, time=0):
        self.value, self.time = value, time

    @classmethod
    def unit(cls, value):
        return cls(value)

    def bind(self, f):
        timed_value = f(self.value)
        new_value = timed_value.value
        new_time = self.time + timed_value.time
        return TimedValue(new_value, new_time)


timed_value = (
    fast(1)
    .bind(slow)
    .bind(slow2)
)
value, time = timed_value.value, timed_value.time
