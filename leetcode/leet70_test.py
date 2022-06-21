import unittest

from leet70 import Leet70


class TestLeet70(unittest.TestCase):
    def setUp(self):
        self.leet70 = Leet70()

    def test_climb_stairs_1(self):
        test = self.leet70.climb_stairs(2)
        self.assertEqual(test, 2)

    def test_climb_stairs_2(self):
        test = self.leet70.climb_stairs(3)
        self.assertEqual(test, 3)

    def test_climb_stairs_3(self):
        test = self.leet70.climb_stairs(4)
        self.assertEqual(test, 5)


if __name__ == "__main__":
    unittest.main()
