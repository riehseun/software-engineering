import unittest

from leet128 import Leet128


class TestLeet128(unittest.TestCase):
    def setUp(self):
        self.leet128 = Leet128()

    def test_longest_consecutive_1(self):
        test = self.leet128.longest_consecutive([100,4,200,1,3,2])
        self.assertEqual(test, 4)

    def test_longest_consecutive_2(self):
        test = self.leet128.longest_consecutive([0,3,7,2,5,8,4,6,0,1])
        self.assertEqual(test, 9)


if __name__ == "__main__":
    unittest.main()
