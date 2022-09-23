import unittest

from leet32 import Leet32


class TestLeet32(unittest.TestCase):
    def setUp(self):
        self.leet32 = Leet32()

    def test_longest_valid_parentheses_1(self):
        test = self.leet32.longest_valid_parentheses("(()")
        self.assertEqual(test, 2)

    def test_longest_valid_parentheses_2(self):
        test = self.leet32.longest_valid_parentheses(")()())")
        self.assertEqual(test, 4)

    def test_longest_valid_parentheses_3(self):
        test = self.leet32.longest_valid_parentheses("")
        self.assertEqual(test, 0)

    def test_longest_valid_parentheses_4(self):
        test = self.leet32.longest_valid_parentheses("()(()")
        self.assertEqual(test, 2)

    def test_longest_valid_parentheses_5(self):
        test = self.leet32.longest_valid_parentheses("()(())")
        self.assertEqual(test, 6)

    def test_longest_valid_parentheses_6(self):
        test = self.leet32.longest_valid_parentheses("())")
        self.assertEqual(test, 2)


if __name__ == "__main__":
    unittest.main()
