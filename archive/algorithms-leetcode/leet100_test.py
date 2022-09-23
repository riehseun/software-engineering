import unittest

from leet100 import Leet100
from treenode import TreeNode


class TestLeet100(unittest.TestCase):
    def setUp(self):
        self.leet100 = Leet100()

    def test_is_same_tree_1(self):
        node6 = TreeNode(3,None,None)
        node5 = TreeNode(2,None,None)
        node4 = TreeNode(1,node5,node6)
        node3 = TreeNode(3,None,None)
        node2 = TreeNode(2,None,None)
        node1 = TreeNode(1,node2,node3)
        test = self.leet100.is_same_tree(node1, node4)
        self.assertEqual(test, True)

    def test_is_same_tree_2(self):
        node4 = TreeNode(2,None,None)
        node3 = TreeNode(1,None,node4)
        node2 = TreeNode(2,None,None)
        node1 = TreeNode(1,node2,None)
        test = self.leet100.is_same_tree(node1, node3)
        self.assertEqual(test, False)

    def test_is_same_tree_3(self):
        node6 = TreeNode(2,None,None)
        node5 = TreeNode(1,None,None)
        node4 = TreeNode(1,node5,node6)
        node3 = TreeNode(1,None,None)
        node2 = TreeNode(2,None,None)
        node1 = TreeNode(1,node2,node3)
        test = self.leet100.is_same_tree(node1, node4)
        self.assertEqual(test, False)


if __name__ == "__main__":
    unittest.main()
