from concurrent import futures
import random


def compute():
    return sum([random.randint(1, 100) for i in range(1000000)])


with futures.ThreadPoolExecutor(max_workers=8) as executor:
    computed_futures = [executor.submit(compute) for _ in range(8)]


results = [f.result() for f in computed_futures]


print('Results: {}'.format(results))
