from something import Something
from something import bar
from something import foo


def test_foo():
  assert 'foo' == foo()


def test_bar():
  assert 'bar' == bar()


class TestSomething:
  test_instance = None

  @classmethod
  def setup_class(cls):
    print 'setup class'
    cls.test_instance = Something(10)

  @classmethod
  def teardown_class(cls):
    print 'teardown class'

  def test_foo(self):
    print 'test foo'
    assert 10 == self.test_instance.foo()

  def test_bar(self):
    print 'test bar'
    self.test_instance.bar(5)
    assert 5 == self.test_instance.foo()
    self.test_instance.bar(10)  # necessary for test_foo(). nosetests run tests in alphabetical order
