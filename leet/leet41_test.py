import unittest

from leet41 import Leet41


class TestLeet37(unittest.TestCase):
    def setUp(self):
        self.leet41 = Leet41()

    def test_first_missing_positive_1(self):
        test = self.leet41.first_missing_positive([1,4,3,3,3])
        self.assertEqual(test, 2)

    def test_first_missing_positive_2(self):
        test = self.leet41.first_missing_positive([3,4,-1,1])
        self.assertEqual(test, 2)

    def test_first_missing_positive_3(self):
        test = self.leet41.first_missing_positive([1,2,0])
        self.assertEqual(test, 3)

    def test_first_missing_positive_4(self):
        test = self.leet41.first_missing_positive([1,2,3])
        self.assertEqual(test, 4)

    def test_first_missing_positive_5(self):
        test = self.leet41.first_missing_positive([7,8,9,11,12])
        self.assertEqual(test, 1)


if __name__ == "__main__":
    unittest.main()
