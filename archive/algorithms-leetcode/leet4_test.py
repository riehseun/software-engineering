import unittest

from leet4 import Leet4


class TestLeet4(unittest.TestCase):
    def setUp(self):
        self.leet4 = Leet4()

    def test_find_median_sorted_arrays_1(self):
        test = self.leet4.find_median_sorted_arrays([1,3], [2])
        self.assertEqual(test, 2.00000)

    def test_find_median_sorted_arrays_2(self):
        test = self.leet4.find_median_sorted_arrays([1,2], [3,4])
        self.assertEqual(test, 2.50000)

    def test_find_median_sorted_arrays_3(self):
        test = self.leet4.find_median_sorted_arrays([1,2,3,5,7], [3,4,6,9,11])
        self.assertEqual(test, 4.50000)

    def test_find_median_sorted_arrays_4(self):
        test = self.leet4.find_median_sorted_arrays([], [1])
        self.assertEqual(test, 1.00000)

    def test_find_median_sorted_arrays_5(self):
        test = self.leet4.find_median_sorted_arrays([0,0,0,0,0], [-1,0,0,0,0,0,1])
        self.assertEqual(test, 0.00000)

    def test_find_median_sorted_arrays_6(self):
        test = self.leet4.find_median_sorted_arrays([1,2], [-1,3])
        self.assertEqual(test, 1.50000)

    def test_find_median_sorted_arrays_7(self):
        test = self.leet4.find_median_sorted_arrays([1,2], [1,2,3])
        self.assertEqual(test, 2.00000)

    def test_find_median_sorted_arrays_8(self):
        test = self.leet4.find_median_sorted_arrays([1], [2,3])
        self.assertEqual(test, 2.00000)

    def test_find_median_sorted_arrays_9(self):
        test = self.leet4.find_median_sorted_arrays([2], [1,3,4])
        self.assertEqual(test, 2.50000)

    def test_find_median_sorted_arrays_10(self):
        test = self.leet4.find_median_sorted_arrays([1,3], [2,4,5,6])
        self.assertEqual(test, 3.50000)


    def test_find_median_sorted_arrays_11(self):
        test = self.leet4.find_median_sorted_arrays([1,5], [2,3,4,6])
        self.assertEqual(test, 3.50000)

    def test_find_median_sorted_arrays_12(self):
        test = self.leet4.find_median_sorted_arrays([2,4,5], [1,3])
        self.assertEqual(test, 3.00000)

    def test_find_median_sorted_arrays_13(self):
        test = self.leet4.find_median_sorted_arrays([2,6], [1,3,4,5])
        self.assertEqual(test, 3.50000)

    def test_find_median_sorted_arrays_14(self):
        test = self.leet4.find_median_sorted_arrays([2,7], [1,3,4,5,6])
        self.assertEqual(test, 4.00000)


if __name__ == "__main__":
    unittest.main()