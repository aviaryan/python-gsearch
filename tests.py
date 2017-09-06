# -*- coding: utf-8 -*-

import unittest

from googlesearch import search


class TestSearch(unittest.TestCase):

	def test_results_count(self):
		res = search('Avi Aryan', num_results=20)
		self.assertTrue(len(res) > 10, 'Less than 11 results returned')

	def test_results_zero(self):
		res = search('dsjaksfajsdhkhawkehkajdwek')
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
