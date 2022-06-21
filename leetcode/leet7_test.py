import unittest

from leet7 import Leet7


class TestLeet7(unittest.TestCase):
    def setUp(self):
        self.leet7 = Leet7()

    def test_reverse_1(self):
        test = self.leet7.reverse(123)
        self.assertEqual(test, 321)

    def test_reverse_2(self):
        test = self.leet7.reverse(-123)
        self.assertEqual(test, -321)

    def test_reverse_3(self):
        test = self.leet7.reverse(120)
        self.assertEqual(test, 21)


if __name__ == "__main__":
    unittest.main()
