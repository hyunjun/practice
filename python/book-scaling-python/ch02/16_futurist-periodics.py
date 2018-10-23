from futurist import periodics
import time


# periodically scheduling function


@periodics.periodic(1)
def every_one(started_at):
    print('1: {}'.format(time.time() - started_at))


w = periodics.PeriodicWorker([(every_one, (time.time(),), {}),])


@periodics.periodic(4)
def print_stats():
    print('stats: {}'.format(list(w.iter_watchers())))


w.add(print_stats)
w.start()
