from unittest import TestCase
from twill_decorator import twill_test

class web_tests(TestCase):
	@twill_test
	def test_slashdot(self):
		"""
		go http://slashdot.org
		find this_does_not_exist
		"""
