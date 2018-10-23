import random
import multiprocessing


#   multiprocessing much faster than multithreading if parallelization is possible


def compute(results):
    results.append(sum([random.randint(1, 100) for i in range(1000000)]))


with multiprocessing.Manager() as manager:
    results = manager.list()
    workers = [multiprocessing.Process(target=compute, args=(results,)) for x in range(8)]
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()
    print('Results: {}'.format(results))
