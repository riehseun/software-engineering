import unittest

from leet1423 import Leet1423


class TestLeet1423(unittest.TestCase):
    def setUp(self):
        self.leet1423 = Leet1423()

    def test_max_score_1(self):
        test = self.leet1423.max_score([1,2,3,4,5,6,1], 3)
        self.assertEqual(test, 12)

    def test_max_score_2(self):
        test = self.leet1423.max_score([2,2,2], 2)
        self.assertEqual(test, 4)

    def test_max_score_3(self):
        test = self.leet1423.max_score([9,7,7,9,7,7,9], 7)
        self.assertEqual(test, 55)

    def test_max_score_4(self):
        test = self.leet1423.max_score([96,90,41,82,39,74,64,50,30], 8)
        self.assertEqual(test, 536)


if __name__ == "__main__":
    unittest.main()
