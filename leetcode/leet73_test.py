import unittest

from leet73 import Leet73


class TestLeet73(unittest.TestCase):
    def setUp(self):
        self.leet73 = Leet73()

    def test_set_zeroes_1(self):
        test = [[1,1,1],[1,0,1],[1,1,1]]
        self.leet73.set_zeroes(test)
        self.assertEqual(test, [[1,0,1],[0,0,0],[1,0,1]])

    def test_set_zeroes_2(self):
        test = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        self.leet73.set_zeroes(test)
        self.assertEqual(test, [[0,0,0,0],[0,4,5,0],[0,3,1,0]])


if __name__ == "__main__":
    unittest.main()
