#   https://pymotw.com/3/multiprocessing/communication.html
import multiprocessing


class MyFancyClass:

  def __init__(self, name):
    self.name = name

  def do_something(self):
    proc_name = multiprocessing.current_process().name
    print('Doing something fancy in {} for {}!'.format( proc_name, self.name))


def worker(q):
  obj = q.get()
  obj.do_something()


if __name__ == '__main__':
  queue = multiprocessing.Queue()

  p = multiprocessing.Process(target=worker, args=(queue,))
  p.start()

  queue.put(MyFancyClass('Fancy Dan'))

  # Wait for the worker to finish
  queue.close()
  queue.join_thread()
  p.join()
