import unittest

from leet27 import Leet27


class TestLeet27(unittest.TestCase):
	def setUp(self):
		self.leet27 = Leet27()

	def test_remove_element_1(self):
		test = self.leet27.remove_element([3,2,2,3], 3)
		self.assertEqual(test, 2)

	def test_remove_element_2(self):
		test = self.leet27.remove_element([0,1,2,2,3,0,4,2], 2)
		self.assertEqual(test, 5)


if __name__ == "__main__":
	unittest.main()