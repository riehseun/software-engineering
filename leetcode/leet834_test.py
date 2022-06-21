import unittest

from leet834 import Leet834


class TestLeet834(unittest.TestCase):
    def setUp(self):
        self.leet834 = Leet834()

    def test_sum_of_distances_in_tree_1(self):
        test = self.leet834.sum_of_distances_in_tree(
            6, [[0,1],[0,2],[2,3],[2,4],[2,5]])
        self.assertEqual(test, [8,12,6,10,10,10])


if __name__ == "__main__":
    unittest.main()
