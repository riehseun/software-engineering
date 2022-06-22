import unittest

from leet10 import Leet10


class TestLeet10(unittest.TestCase):
    def setUp(self):
        self.leet10 = Leet10()

    def test_is_match_1(self):
        test = self.leet10.is_match("aa", "a")
        self.assertEqual(test, False)

    def test_is_match_2(self):
        test = self.leet10.is_match("aa", "a*")
        self.assertEqual(test, True)

    def test_is_match_3(self):
        test = self.leet10.is_match("ab", ".*")
        self.assertEqual(test, True)

    def test_is_match_4(self):
        test = self.leet10.is_match("aab", "c*a*b")
        self.assertEqual(test, False)


if __name__ == "__main__":
    unittest.main()
