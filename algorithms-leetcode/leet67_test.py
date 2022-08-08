import unittest

from leet67 import Leet67


class TestLeet67(unittest.TestCase):
    def setUp(self):
        self.leet67 = Leet67()

    def test_add_binary_1(self):
        test = self.leet67.add_binary("11", "1")
        self.assertEqual(test, "100")

    def test_add_binary_2(self):
        test = self.leet67.add_binary("1010", "1011")
        self.assertEqual(test, "10101")


if __name__ == "__main__":
    unittest.main()
