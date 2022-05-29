import unittest

from leet88 import Leet88


class TestLeet88(unittest.TestCase):
    def setUp(self):
        self.leet88 = Leet88()

    def test_merge_1(self):
        test = self.leet88.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
        self.assertEqual(test, [1,2,2,3,5,6])

    def test_merge_2(self):
        test = self.leet88.merge([1], 1, [], 0)
        self.assertEqual(test, [1])

    def test_merge_3(self):
        test = self.leet88.merge([0], 0, [1], 1)
        self.assertEqual(test, [1])

    def test_merge_4(self):
        test = self.leet88.merge([1,0], 1, [2], 1)
        self.assertEqual(test, [1,2])

    def test_merge_5(self):
        test = self.leet88.merge([2,0], 1, [1], 1)
        self.assertEqual(test, [1,2])


if __name__ == "__main__":
    unittest.main()
