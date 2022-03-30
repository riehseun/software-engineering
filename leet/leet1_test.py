import unittest

from leet1 import Leet1


class TestLeet1(unittest.TestCase):
    def setUp(self):
        self.leet1 = Leet1()

    def test_two_sum_1(self):
        test = self.leet1.two_sum([2,7,11,15], 9)
        self.assertEqual(test, [0,1])

    def test_two_sum_2(self):
        test = self.leet1.two_sum([3,2,4], 6)
        self.assertEqual(test, [1,2])

    def test_two_sum_3(self):
        test = self.leet1.two_sum([3,3], 6)
        self.assertEqual(test, [0,1])


if __name__ == "__main__":
    unittest.main()
