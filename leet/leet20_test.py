import unittest

from leet20 import Leet20


class TestLeet20(unittest.TestCase):
    def setUp(self):
        self.leet20 = Leet20()

    def test_is_valid_1(self):
        test = self.leet20.is_valid("()")
        self.assertEqual(test, True)

    def test_is_valid_2(self):
        test = self.leet20.is_valid("()[]()")
        self.assertEqual(test, True)

    def test_is_valid_3(self):
        test = self.leet20.is_valid("(]")
        self.assertEqual(test, False)

    def test_is_valid_4(self):
        test = self.leet20.is_valid("]")
        self.assertEqual(test, False)

    def test_is_valid_5(self):
        test = self.leet20.is_valid("(])")
        self.assertEqual(test, False)


if __name__ == "__main__":
    unittest.main()