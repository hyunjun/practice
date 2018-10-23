import random
import threading


#   multithreading cannot use full core because of GIL


results = []


def compute():
    results.append(sum([random.randint(1, 100) for i in range(1000000)]))


workers = [threading.Thread(target=compute) for x in range(8)]
for worker in workers:
    worker.start()
for worker in workers:
    worker.join()
print('Results: {}'.format(results))
