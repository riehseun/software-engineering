import unittest

from leet17 import Leet17


class TestLeet17(unittest.TestCase):
    def setUp(self):
        self.leet17 = Leet17()

    def test_letter_combinations_1(self):
        test = self.leet17.letter_combinations("23")
        self.assertEqual(test, ["ad","bd","cd","ae","be","ce","af","bf","cf"])

    def test_letter_combinations_2(self):
        test = self.leet17.letter_combinations("")
        self.assertEqual(test, [])

    def test_letter_combinations_3(self):
        test = self.leet17.letter_combinations("2")
        self.assertEqual(test, ["a","b","c"])


if __name__ == "__main__":
    unittest.main()
