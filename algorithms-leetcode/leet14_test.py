import unittest

from leet14 import Leet14


class TestLeet14(unittest.TestCase):
    def setUp(self):
        self.leet14 = Leet14()

    def test_is_palindrom_1(self):
        test = self.leet14.longest_common_prefix(["flower","flow","flight"])
        self.assertEqual(test, "fl")

    def test_is_palindrom_2(self):
        test = self.leet14.longest_common_prefix(["dog","racecar","car"])
        self.assertEqual(test, "")

    def test_is_palindrom_3(self):
        test = self.leet14.longest_common_prefix(["cir","car"])
        self.assertEqual(test, "c")


if __name__ == "__main__":
    unittest.main()