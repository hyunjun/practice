import os
import sys
import py.test


sys.path.append(os.path.join('.', '..'))


import foo


def test_foo():
  assert 'foo' == foo.foo()


def test_bar():
  assert 'bar' == foo.bar()
