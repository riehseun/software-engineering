import unittest

from leet22 import Leet22


class TestLeet22(unittest.TestCase):
    def setUp(self):
        self.leet22 = Leet22()

    def test_generate_parenthesis_1(self):
        test = self.leet22.generate_parenthesis(3)
        self.assertEqual(test, ["((()))","(()())","(())()","()(())","()()()"])

    def test_generate_parenthesis_2(self):
        test = self.leet22.generate_parenthesis(1)
        self.assertEqual(test, ["()"])


if __name__ == "__main__":
    unittest.main()
