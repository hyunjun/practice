from futurist import rejection
import futurist
import random


# limit the max size of queue to avoid memory overflow

# this exception may happen
# futurist._futures.RejectedSubmission: Current backlog 2 is not allowed to go beyond 2


def compute():
    return sum([random.randint(1, 100) for i in range(1000000)])


with futurist.ThreadPoolExecutor(max_workers=8, check_and_reject=rejection.reject_when_reached(2)) as executor:
    futures = [executor.submit(compute) for _ in range(20)]
    print(executor.statistics)


results = waiters.wait_for_all(futures)
print(executor.statistics)


print('Results: {}'.format([r.result() for r in results.done]))
