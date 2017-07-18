import os
import sys
import py.test


sys.path.append(os.path.join('.', '..',))


from app import api_only_flask


def test_api_root():
  assert api_only_flask.api_root() == 'Welcome'
