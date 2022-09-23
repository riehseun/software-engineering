import unittest

from leet101 import Leet101
from treenode import TreeNode


class TestLeet101(unittest.TestCase):
    def setUp(self):
        self.leet101 = Leet101()

    def test_is_symmetric_1(self):
        node7 = TreeNode(3, None, None)
        node6 = TreeNode(4, None, None)
        node5 = TreeNode(4, None, None)
        node4 = TreeNode(3, None, None)
        node3 = TreeNode(2, node6, node7)
        node2 = TreeNode(2, node4, node5)
        node1 = TreeNode(1, node2, node3)
        test = self.leet101.is_symmetric(node1)
        self.assertEqual(test, True)

    def test_is_symmetric_2(self):
        node5 = TreeNode(3, None, None)
        node4 = TreeNode(3, None, None)
        node3 = TreeNode(2, None, node5)
        node2 = TreeNode(2, None, node4)
        node1 = TreeNode(1, node2, node3)
        test = self.leet101.is_symmetric(node1)
        self.assertEqual(test, False)


if __name__ == "__main__":
    unittest.main()
