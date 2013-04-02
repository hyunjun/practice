'''
Execution: nosetests -v wrap_test2.py
'''
from unittest import TestCase
from functools import wraps

def twill_ex(func):
	'''
	This function name should not have 'test'
	It being twill_test, python returns error like below;
	TypeError: twill_test() takes exactly 1 argument (0 given)
	'''
	@wraps(func)
	def run_test(*args):
		pass
	return run_test

class web_tests(TestCase):
	@twill_ex
	def test_slashdot(self):
		pass
