from concurrent import futures
import random


#   do not need to set max_workers because concurrent.futures decide it by calling multiprocessing.cpu_count


def compute():
    return sum([random.randint(1, 100) for i in range(1000000)])


with futures.ProcessPoolExecutor() as executor:
    computed_futures = [executor.submit(compute) for _ in range(8)]


results = [f.result() for f in computed_futures]


print('Results: {}'.format(results))
