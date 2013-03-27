from unittest import TestCase
import twill

'''
import os
import sys
sys.path.append(os.path.abspath('/usr/local/etc/twill-0.9/twill')
'''

class test_twill_browser(TestCase):
	def setUp(self):
		import os
		import sys
		sys.path.append(os.path.abspath('/usr/local/etc/twill-0.9/twill')

	def test_slashdot(self):
		browser = twill.get_browser()
		browser.go('http://slashdot.org/')
		self.assertTrue(browser.get_code() in (200, 201))
		html = browser.get_html()
		self.assertTrue(html.count('slashdot') > 150)
		link = browser.find_link('Science')
		browser.follow_link(link)
		form = browser.get_form(2)
		form.set_value('aardvark', name='fhfilter')
		browser.clicked(form, None)
		browser.submit()
		self.assertEqual(browser.get_code(), 200)
