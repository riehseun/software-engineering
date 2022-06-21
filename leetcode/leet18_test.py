import unittest

from leet18 import Leet18


class TestLeet18(unittest.TestCase):
    def setUp(self):
        self.leet18 = Leet18()

    def test_four_sum_1(self):
        test = self.leet18.four_sum([1,0,-1,0,-2,2], 0)
        self.assertEqual(test, [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])

    def test_four_sum_2(self):
        test = self.leet18.four_sum([2,2,2,2,2], 8)
        self.assertEqual(test, [[2,2,2,2]])


if __name__ == "__main__":
    unittest.main()
