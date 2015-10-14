def foo():
  return 'foo'

def bar():
  return 'bar'


class Something:

  def __init__(self, i):
    self.i = i

  def foo(self):
    return self.i

  def bar(self, i):
    self.i = i


if __name__ == '__main__':
  print foo(), bar()
  something = Something(10)
  print something.foo()
  something.bar(5)
  print something.foo()
