import unittest

from leet58 import Leet58


class TestLeet58(unittest.TestCase):
    def setUp(self):
        self.leet58 = Leet58()

    def test_length_of_last_word_1(self):
        test = self.leet58.length_of_last_word("Hello World")
        self.assertEqual(test, 5)

    def test_length_of_last_word_2(self):
        test = self.leet58.length_of_last_word("   fly me   to   the moon  ")
        self.assertEqual(test, 4)

    def test_length_of_last_word_3(self):
        test = self.leet58.length_of_last_word("luffy is still joyboy")
        self.assertEqual(test, 6)


if __name__ == "__main__":
    unittest.main()