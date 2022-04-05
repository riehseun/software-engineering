import unittest

from leet53 import Leet53


class TestLeet53(unittest.TestCase):
    def setUp(self):
        self.leet53 = Leet53()

    def test_max_sub_array_1(self):
        test = self.leet53.max_sub_array([-2,1,-3,4,-1,2,1,-5,4])
        self.assertEqual(test, 6)

    def test_max_sub_array_2(self):
        test = self.leet53.max_sub_array([1])
        self.assertEqual(test, 1)

    def test_max_sub_array_3(self):
        test = self.leet53.max_sub_array([5,4,-1,7,8])
        self.assertEqual(test, 23)

    def test_max_sub_array_4(self):
        test = self.leet53.max_sub_array([-2, 1])
        self.assertEqual(test, 1)


if __name__ == "__main__":
    unittest.main()
