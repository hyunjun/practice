#   https://pymotw.com/3/multiprocessing/basics.html
import multiprocessing


def worker(num):
  """thread worker function"""
  print('Worker:', num)


if __name__ == '__main__':
  jobs = []
  for i in range(5):
    p = multiprocessing.Process(target=worker, args=(i,))
    jobs.append(p)
    p.start()
