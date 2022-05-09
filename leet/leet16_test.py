import unittest

from leet16 import Leet16


class TestLeet16(unittest.TestCase):
    def setUp(self):
        self.leet16 = Leet16()

    def test_three_sum_closest_1(self):
        test = self.leet16.three_sum_closest([-1,2,1,-4], 1)
        self.assertEqual(test, 2)

    def test_three_sum_closest_2(self):
        test = self.leet16.three_sum_closest([0,0,0], 1)
        self.assertEqual(test, 0)

    def test_three_sum_closest_3(self):
        test = self.leet16.three_sum_closest([1,1,1,0], 100)
        self.assertEqual(test, 3)

    def test_three_sum_closest_4(self):
        test = self.leet16.three_sum_closest([0,2,1,-3], 1)
        self.assertEqual(test, 0)

    def test_three_sum_closest_5(self):
        test = self.leet16.three_sum_closest([1,1,-1,-1,3], -1)
        self.assertEqual(test, -1)


if __name__ == "__main__":
    unittest.main()
