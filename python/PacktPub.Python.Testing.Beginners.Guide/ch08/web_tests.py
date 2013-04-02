from unittest import TestCase
#from twill_decorator import twill_test
from twill.commands import go

from twill_test import twill_ex

class web_tests(TestCase):
	'''
	execution: nosetests -v web_tests.py
	'''
	@twill_ex
	def test_slashdot(self):
		"""
		go http://slashdot.org
		find this_does_not_exist
		"""
