import unittest

from leet28 import Leet28


class TestLeet28(unittest.TestCase):
	def setUp(self):
		self.leet28 = Leet28()

	def test_str_str_1(self):
		test = self.leet28.str_str("hello", "ll")
		self.assertEqual(test, 2)

	def test_str_str_2(self):
		test = self.leet28.str_str("aaaaa", "bba")
		self.assertEqual(test, -1)


if __name__ == "__main__":
	unittest.main()