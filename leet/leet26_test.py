import unittest
import math

from leet26 import Leet26


class TestLeet26(unittest.TestCase):
    def setUp(self):
        self.leet26 = Leet26()

    def test_remove_duplicates_1(self):
        test = self.leet26.remove_duplicates([1,1,2])
        inf = math.inf
        # [1,2,inf]
        self.assertEqual(test, 2)

    def test_remove_duplicates_2(self):
        test = self.leet26.remove_duplicates([0,0,1,1,1,2,2,3,3,4])
        inf = math.inf
        # [0,1,2,3,4,inf,inf,inf,inf,inf]
        self.assertEqual(test, 5)

    def test_remove_duplicates_3(self):
        test = self.leet26.remove_duplicates([1])
        inf = math.inf
        # [1]
        self.assertEqual(test, 1)

    def test_remove_duplicates_4(self):
        test = self.leet26.remove_duplicates([1,2])
        inf = math.inf
        # [1,2]
        self.assertEqual(test, 2)

    def test_remove_duplicates_5(self):
        test = self.leet26.remove_duplicates([1,2,3])
        inf = math.inf
        # [1,2,3]
        self.assertEqual(test, 3)


if __name__ == "__main__":
    unittest.main()
