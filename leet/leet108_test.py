import unittest

from leet108 import Leet108
from treenode import TreeNode


class TestLeet108(unittest.TestCase):
    def setUp(self):
        self.leet108 = Leet108()

    def test_sorted_array_to_bst_1(self):
        # node4 = TreeNode(7,None,None)
        # node3 = TreeNode(15,None,None)
        # node2 = TreeNode(20,node3,node4)
        # node1 = TreeNode(9,None,None)
        # root = TreeNode(3,node1,node2)
        # test = self.leet108.sorted_array_to_bst([-10,-3,0,5,9])
        # self.assertEqual(test, 3)


if __name__ == "__main__":
    unittest.main()
