# -*- coding: utf-8 -*-

import unittest
import time
from random import randint

from gsearch.googlesearch import search


class TestSearch(unittest.TestCase):

	def setUp(self):
		time.sleep(randint(15,20))

	def test_results_count(self):
		res = search('Avi Aryan', num_results=30)
		self.assertTrue(len(res) > 10, 'Less than 11 results returned')

	def test_results_zero(self):
		res = search('dsjaksfajsdhkhawkehkajdwek' + (str(randint(10,100)) * 5))
		self.assertTrue(len(res) == 0, 'There was a result. What has this world come to?')

	def test_unicode(self):
		res = search('君の名')
		self.assertTrue(len(res) > 0)
		# found = False
		# for r in res:
		# 	found = r[0].find('君の名') > -1
		# self.assertTrue(found)



if __name__ == '__main__':
	unittest.main()
