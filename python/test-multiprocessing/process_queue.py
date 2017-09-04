#   https://stackoverflow.com/questions/8489684/python-subclassing-multiprocessing-process
from multiprocessing import Process, Queue


class Processor(Process):

  def __init__(self, queue, idx, **kwargs):
    super(Processor, self).__init__()
    self.queue = queue
    self.idx = idx
    self.kwargs = kwargs

  def run(self):
    """Build some CPU-intensive tasks to run via multiprocessing here."""

    #   TypeError: unhashable type: 'dict'
    #hash(self.kwargs) # Shameless usage of CPU for no gain...

    ## Return some information back through multiprocessing.Queue
    ## NOTE: self.name is an attribute of multiprocessing.Process
    self.queue.put("Process idx={0} is called '{1}'".format(self.idx, self.name))

if __name__ == "__main__":
  NUMBER_OF_PROCESSES = 5

  ## Create a list to hold running Processor object instances...
  processes = list()

  q = Queue() # Build a single queue to send to all process objects...
  for i in range(0, NUMBER_OF_PROCESSES):
    p=Processor(queue=q, idx=i)
    p.start()
    processes.append(p)

  # Incorporating ideas from this answer, below...
  #    https://stackoverflow.com/a/42137966/667301
  [proc.join() for proc in processes]
  while not q.empty():
    print("RESULT: {0}".format(q.get())) #   get results from the queue...
