import unittest

from leet11 import Leet11


class TestLeet11(unittest.TestCase):
    def setUp(self):
        self.leet11 = Leet11()

    def test_max_area_1(self):
        test = self.leet11.max_area([1,8,6,2,5,4,8,3,7])
        self.assertEqual(test, 49)

    def test_max_area_2(self):
        test = self.leet11.max_area([1,1])
        self.assertEqual(test, 1)

    def test_max_area_3(self):
        test = self.leet11.max_area([2,3,10,5,7,8,9])
        self.assertEqual(test, 36)


if __name__ == "__main__":
    unittest.main()
