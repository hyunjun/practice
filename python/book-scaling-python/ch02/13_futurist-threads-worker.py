from futurist import waiters
import futurist
import random


#   pip install futurist


def compute():
    return sum([random.randint(1, 100) for i in range(1000000)])


with futurist.ThreadPoolExecutor(max_workers=8) as executor:
    futures = [executor.submit(compute) for _ in range(8)]


results = waiters.wait_for_all(futures)
print(executor.statistics)


print('Results: {}'.format([r.result() for r in results.done]))
