import unittest

from leet15 import Leet15


class TestLeet15(unittest.TestCase):
    def setUp(self):
        self.leet15 = Leet15()

    def test_three_sum_1(self):
        test = self.leet15.three_sum([-1,0,1,2,-1,-4])
        self.assertEqual(test, [[-1,-1,2], [0,-1,1]])

    def test_three_sum_2(self):
        test = self.leet15.three_sum([])
        self.assertEqual(test, [])

    def test_three_sum_3(self):
        test = self.leet15.three_sum([0])
        self.assertEqual(test, [])

    def test_three_sum_4(self):
        test = self.leet15.three_sum([0,0,0])
        self.assertEqual(test, [[0,0,0]])

    def test_three_sum_5(self):
        test = self.leet15.three_sum(
            [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0])
        self.assertEqual(
            test, [[-2,-2,4], [0,-4,4], [0,0,0], [1,-5,4], [1,-4,3], [1,-2,1]])


if __name__ == "__main__":
    unittest.main()
