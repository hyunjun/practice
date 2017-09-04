#   https://pymotw.com/3/multiprocessing/basics.html
import multiprocessing
import logging
import sys


def worker():
  print('Doing some work')
  sys.stdout.flush()


if __name__ == '__main__':
  multiprocessing.log_to_stderr()
  logger = multiprocessing.get_logger()
  logger.setLevel(logging.INFO)
  p = multiprocessing.Process(target=worker)
  p.start()
  p.join()
