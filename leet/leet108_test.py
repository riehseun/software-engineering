import unittest

from leet108 import Leet108
from treenode import TreeNode


class TestLeet108(unittest.TestCase):
    def setUp(self):
        self.leet108 = Leet108()

    def test_sorted_array_to_bst_1(self):
        node5 = TreeNode(5,None,None)
        node4 = TreeNode(-10,None,None)
        node3 = TreeNode(9,node5,None)
        node2 = TreeNode(-3,node4,None)
        node1 = TreeNode(0,node2,node3)
        test = self.leet108.sorted_array_to_bst([-10,-3,0,5,9])
        self.assertEqual(test.val, 0)


if __name__ == "__main__":
    unittest.main()
