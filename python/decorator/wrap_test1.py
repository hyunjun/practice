'''
http://stackoverflow.com/questions/7727678/nose-ignores-test-with-custom-decorator
http://www.outofwhatbox.com/blog/2010/07/python-decorating-with-class/

Execution: nosetests -v wrap_test.py
'''
from unittest import TestCase
from functools import wraps

def specialTest(fn):
    @wraps(fn)
    def test_wrapper(self,*args,**kwargs):
        pass
    return test_wrapper

class Test_special_stuff(TestCase):
    @specialTest
    def test_something_special(self):
        pass
