import unittest

from leet21 import Leet21


class TestLeet21(unittest.TestCase):
	def setUp(self):
		self.leet21 = Leet21()

	def test_merge_two_lists_1(self):
		test = self.leet21.merge_two_lists([1,2,4], [1,3,4])
		self.assertEqual(test, [1,1,2,3,4,4])

	def test_merge_two_lists_2(self):
		test = self.leet21.merge_two_lists([], [])
		self.assertEqual(test, [])

	def test_merge_two_lists_3(self):
		test = self.leet21.merge_two_lists([], [0])
		self.assertEqual(test, [0])


if __name__ == "__main__":
	unittest.main()