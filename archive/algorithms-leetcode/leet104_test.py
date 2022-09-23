import unittest

from leet104 import Leet104
from treenode import TreeNode


class TestLeet104(unittest.TestCase):
    def setUp(self):
        self.leet104 = Leet104()

    def test_max_depth_1(self):
        node4 = TreeNode(7,None,None)
        node3 = TreeNode(15,None,None)
        node2 = TreeNode(20,node3,node4)
        node1 = TreeNode(9,None,None)
        root = TreeNode(3,node1,node2)
        test = self.leet104.max_depth(root)
        self.assertEqual(test, 3)

    def test_max_depth_2(self):
        node2 = TreeNode(2, None, None)
        node1 = TreeNode(1, None, node2)
        test = self.leet104.max_depth(node1)
        self.assertEqual(test, 2)


if __name__ == "__main__":
    unittest.main()
