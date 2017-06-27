# -*- coding: utf8 -*-
import os
import sys
import py.test


sys.path.append(os.path.join('.', '..', '..', '..'))


from common.src import common


def test_remove_blank_and_make_lower():
  assert 'abc하하xyz' == common.remove_blank_and_make_lower('aBc 하하 XYZ')
