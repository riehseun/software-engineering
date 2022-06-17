import unittest

from leet111 import Leet111
from treenode import TreeNode


class TestLeet111(unittest.TestCase):
    def setUp(self):
        self.leet111 = Leet111()

    def test_min_depth_1(self):
        node5 = TreeNode(7,None,None)
        node4 = TreeNode(15,None,None)
        node3 = TreeNode(20,node4,node5)
        node2 = TreeNode(9,None,None)
        node1 = TreeNode(3,node2,node3)
        test = self.leet111.min_depth(node1)
        self.assertEqual(test, 2)


if __name__ == "__main__":
    unittest.main()
