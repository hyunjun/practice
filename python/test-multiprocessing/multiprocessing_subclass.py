#   https://pymotw.com/3/multiprocessing/basics.html
import multiprocessing


class Worker(multiprocessing.Process):

  def run(self):
    print('In {}'.format(self.name))
    return


if __name__ == '__main__':
  jobs = []
  for i in range(5):
    p = Worker()
    jobs.append(p)
    p.start()
  for j in jobs:
    j.join()
