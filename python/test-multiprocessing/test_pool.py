from concurrent.futures import ProcessPoolExecutor
import os


#   Python ProcessPoolExecutors Tutorial
#   https://www.youtube.com/watch?v=J7w_G6ZKzz4
#   https://tutorialedge.net/python/concurrency/python-processpoolexecutor-tutorial/


def task():
    print('Executing task on process {}'.format(os.getpid()))


def main():
    with ProcessPoolExecutor(max_workers=3) as executor:
        task1 = executor.submit(task)
        task2 = executor.submit(task)


main()
