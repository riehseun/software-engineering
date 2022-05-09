import unittest

from leet3 import Leet3


class TestLeet3(unittest.TestCase):
    def setUp(self):
        self.leet3 = Leet3()

    def test_length_of_longest_substring_1(self):
        test = self.leet3.length_of_longest_substring("abcabcbb")
        self.assertEqual(test, 3)

    def test_length_of_longest_substring_2(self):
        test = self.leet3.length_of_longest_substring("bbbbb")
        self.assertEqual(test, 1)

    def test_length_of_longest_substring_3(self):
        test = self.leet3.length_of_longest_substring("pwwkew")
        self.assertEqual(test, 3)

    def test_length_of_longest_substring_4(self):
        test = self.leet3.length_of_longest_substring(" ")
        self.assertEqual(test, 1)

    def test_length_of_longest_substring_5(self):
        test = self.leet3.length_of_longest_substring("au")
        self.assertEqual(test, 2)

    def test_length_of_longest_substring_6(self):
        test = self.leet3.length_of_longest_substring("dvdf")
        self.assertEqual(test, 3)

    def test_length_of_longest_substring_7(self):
        test = self.leet3.length_of_longest_substring("abba")
        self.assertEqual(test, 2)

    def test_length_of_longest_substring_8(self):
        test = self.leet3.length_of_longest_substring("tmmzuxt")
        self.assertEqual(test, 5)


if __name__ == "__main__":
    unittest.main()