import unittest

from leet300 import Leet300


class TestLeet300(unittest.TestCase):
    def setUp(self):
        self.leet300 = Leet300()

    def test_length_of_lis_1(self):
        test = self.leet300.length_of_lis([10,9,2,5,3,7,101,18])
        self.assertEqual(test, 4)

    def test_length_of_lis_2(self):
        test = self.leet300.length_of_lis([0,1,0,3,2,3])
        self.assertEqual(test, 4)

    def test_length_of_lis_3(self):
        test = self.leet300.length_of_lis([7,7,7,7,7,7,7])
        self.assertEqual(test, 1)


if __name__ == "__main__":
    unittest.main()