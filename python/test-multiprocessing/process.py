import multiprocessing as mp

#   https://stackoverflow.com/questions/7545385/python-class-inheriting-multiprocessing-trouble-with-accessing-class-members
class Worker(mp.Process):
  def __init__(self):
    print("Init")
    mp.Process.__init__(self)
    self.num = mp.Value('d', 0.0)

  def run(self):
    print("Running")
    self.num.value = 1

p = Worker()
p.start()
p.join()
print(p.num.value)
