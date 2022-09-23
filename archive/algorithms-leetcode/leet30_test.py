import unittest

from leet30 import Leet30


class TestLeet30(unittest.TestCase):
    def setUp(self):
        self.leet30 = Leet30()

    def test_substring_with_concatenation_of_all_words_1(self):
        test = self.leet30.substring_with_concatenation_of_all_words(
            "barfoothefoobarman", ["foo","bar"])
        self.assertEqual(test, [0,9])

    def test_substring_with_concatenation_of_all_words_2(self):
        test = self.leet30.substring_with_concatenation_of_all_words(
            "wordgoodgoodgoodbestword", ["word","good","best","word"])
        self.assertEqual(test, [])

    def test_substring_with_concatenation_of_all_words_3(self):
        test = self.leet30.substring_with_concatenation_of_all_words(
            "barfoofoobarthefoobarman", ["bar","foo","the"])
        self.assertEqual(test, [6,9,12])

    def test_substring_with_concatenation_of_all_words_4(self):
        test = self.leet30.substring_with_concatenation_of_all_words(
            "wordgoodgoodgoodbestword", ["word","good","best","good"])
        self.assertEqual(test, [8])

    def test_substring_with_concatenation_of_all_words_5(self):
        test = self.leet30.substring_with_concatenation_of_all_words(
            "ababaab", ["ab","ba","ba"])
        self.assertEqual(test, [1])


if __name__ == "__main__":
    unittest.main()
