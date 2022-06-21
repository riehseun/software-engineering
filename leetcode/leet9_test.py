import unittest

from leet9 import Leet9


class TestLeet9(unittest.TestCase):
    def setUp(self):
        self.leet9 = Leet9()

    def test_is_palindrom_1(self):
        test = self.leet9.is_palindrom(121)
        self.assertEqual(test, True)

    def test_is_palindrom_2(self):
        test = self.leet9.is_palindrom(-121)
        self.assertEqual(test, False)

    def test_is_palindrom_3(self):
        test = self.leet9.is_palindrom(10)
        self.assertEqual(test, False)

    def test_is_palindrom_4(self):
        test = self.leet9.is_palindrom(13431)
        self.assertEqual(test, True)

    def test_is_palindrom_5(self):
        test = self.leet9.is_palindrom(13434)
        self.assertEqual(test, False)

    def test_is_palindrom_6(self):
        test = self.leet9.is_palindrom(7)
        self.assertEqual(test, True)

    def test_is_palindrom_7(self):
        test = self.leet9.is_palindrom(11)
        self.assertEqual(test, True)

    def test_is_palindrom_8(self):
        test = self.leet9.is_palindrom(21120)
        self.assertEqual(test, False)

    def test_is_palindrom_9(self):
        test = self.leet9.is_palindrom(0)
        self.assertEqual(test, True)


if __name__ == "__main__":
    unittest.main()
