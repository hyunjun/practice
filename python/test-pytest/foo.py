# -*- coding: utf8 -*-
from __future__ import print_function
from common.src import common


def foo():
  return 'foo'


def bar():
  return 'bar'


if __name__ == '__main__':
  print(foo())
  print(common.remove_blank_and_make_lower('aBc 하하 XYZ'))
