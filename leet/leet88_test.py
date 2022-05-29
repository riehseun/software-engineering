import unittest

from leet88 import Leet88


class TestLeet88(unittest.TestCase):
    def setUp(self):
        self.leet88 = Leet88()

    def test_merge_1(self):
        test = self.leet88.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
        self.assertEqual(test, [1,2,2,3,5,6])


if __name__ == "__main__":
    unittest.main()
