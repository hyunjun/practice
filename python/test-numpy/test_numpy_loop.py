import timeit
import numpy as np

my_arr = np.arange(100)
my_list = list(range(100))

def test():
    for _ in range(10):
        my_arr2 = my_arr * 2

print(timeit.timeit("test()", setup="from __main__ import test"))
