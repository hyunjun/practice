from itertools import islice


# https://mingrammer.com/translation-iterators-vs-generators
class fib:
  def __init__(self):
    self.prev = 0
    self.curr = 1

  def __iter__(self):
    return self

  def __next__(self): # python3
  # def next(self): # python2
    value = self.curr
    self.curr += self.prev
    self.prev = value
    return value


f = fib()
print(list(islice(f, 0, 10)))
