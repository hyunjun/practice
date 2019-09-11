from concurrent.futures import ThreadPoolExecutor
import threading
import time


#   Python ThreadPoolExecutors Tutorial
#   https://tutorialedge.net/python/concurrency/python-threadpoolexecutor-tutorial/


def task():
    time.sleep(1)
    print('Executing task on thread {}'.format(threading.current_thread()))


def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        tasks = [executor.submit(task) for _ in range(10)]

main()
