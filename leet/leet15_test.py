import unittest

from leet15 import Leet15


class TestLeet15(unittest.TestCase):
    def setUp(self):
        self.leet15 = Leet15()

    def test_max_area_1(self):
        test = self.leet15.three_sum([-1,0,1,2,-1,-4])
        self.assertEqual(test, [[-1,-1,2],[-1,0,1]])

    def test_max_area_2(self):
        test = self.leet15.three_sum([])
        self.assertEqual(test, [])

    def test_max_area_3(self):
        test = self.leet15.three_sum([0])
        self.assertEqual(test, [])

    def test_max_area_4(self):
        test = self.leet15.three_sum([0,0,0])
        self.assertEqual(test, [[0,0,0]])


if __name__ == "__main__":
    unittest.main()
