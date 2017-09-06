import unittest

from googlesearch import search


class TestSearch(unittest.TestCase):

	def test_results_count(self):
		res = search('Avi Aryan', num_results=20)
		self.assertTrue(len(res) > 10, 'Less than 11 results returned')

	def test_results_zero(self):
		res = search('dsjaksfajsdhkhawkehkajdwek')
		self.assertTrue(len(res) == 0, 'There was a result. What has this world come to?')


if __name__ == '__main__':
	unittest.main()
