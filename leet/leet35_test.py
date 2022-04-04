import unittest

from leet35 import Leet35


class TestLeet35(unittest.TestCase):
	def setUp(self):
		self.leet35 = Leet35()

	def test_search_insert_1(self):
		test = self.leet35.search_insert([1,3,5,6], 5)
		self.assertEqual(test, 2)

	def test_search_insert_2(self):
		test = self.leet35.search_insert([1,3,5,6], 2)
		self.assertEqual(test, 1)

	def test_search_insert_3(self):
		test = self.leet35.search_insert([1,3,5,6], 7)
		self.assertEqual(test, 4)


if __name__ == "__main__":
	unittest.main()