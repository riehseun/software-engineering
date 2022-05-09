import unittest

from leet5 import Leet5


class TestLeet5(unittest.TestCase):
    def setUp(self):
        self.leet5 = Leet5()

    def test_is_palindrom_1(self):
        test = self.leet5.longest_palindrome("babad")
        self.assertEqual(test, "bab")

    def test_is_palindrom_2(self):
        test = self.leet5.longest_palindrome("cbbd")
        self.assertEqual(test, "bb")

    def test_is_palindrom_3(self):
        test = self.leet5.longest_palindrome("bab")
        self.assertEqual(test, "bab")

    def test_is_palindrom_4(self):
        test = self.leet5.longest_palindrome("a")
        self.assertEqual(test, "a")

    def test_is_palindrom_5(self):
        test = self.leet5.longest_palindrome("ccd")
        self.assertEqual(test, "cc")

    def test_is_palindrom_6(self):
        test = self.leet5.longest_palindrome("eabcb")
        self.assertEqual(test, "bcb")

    def test_is_palindrom_7(self):
        test = self.leet5.longest_palindrome("SQQSYYSQQS")
        self.assertEqual(test, "SQQSYYSQQS")


if __name__ == "__main__":
    unittest.main()
