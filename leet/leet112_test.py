import unittest

from leet112 import Leet112
from treenode import TreeNode


class TestLeet112(unittest.TestCase):
    def setUp(self):
        self.leet112 = Leet112()

    def test_min_depth_1(self):
        node5 = TreeNode(7,None,None)
        node4 = TreeNode(15,None,None)
        node3 = TreeNode(20,node4,node5)
        node2 = TreeNode(9,None,None)
        node1 = TreeNode(3,node2,node3)
        test = self.leet112.has_path_sum(node1, 12)
        self.assertEqual(test, True)


if __name__ == "__main__":
    unittest.main()
