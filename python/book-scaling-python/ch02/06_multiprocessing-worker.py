import random
import multiprocessing


#   functional way by pool


def compute(n):
    return sum([random.randint(1, 100) for i in range(1000000)])


pool = multiprocessing.Pool(processes=8)
print('Results: {}'.format(pool.map(compute, range(8))))
