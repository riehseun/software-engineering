import unittest

from leet49 import Leet49


class TestLeet49(unittest.TestCase):
    def setUp(self):
        self.leet49 = Leet49()

    def test_group_anagrams_1(self):
        test = self.leet49.group_anagrams(["eat","tea","tan","ate","nat","bat"])
        self.assertEqual(test, [["eat","tea","ate"], ["tan","nat"], ["bat"]])

    def test_group_anagrams_2(self):
        test = self.leet49.group_anagrams([""])
        self.assertEqual(test, [[""]])

    def test_group_anagrams_3(self):
        test = self.leet49.group_anagrams(["a"])
        self.assertEqual(test, [["a"]])


if __name__ == "__main__":
    unittest.main()
