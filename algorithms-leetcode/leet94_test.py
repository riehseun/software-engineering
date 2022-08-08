import unittest

from leet94 import Leet94
from treenode import TreeNode


class TestLeet94(unittest.TestCase):
    def setUp(self):
        self.leet94 = Leet94()

    def test_merge_1(self):
        node3 = TreeNode(3,None,None)
        node2 = TreeNode(2,node3,None)
        node1 = TreeNode(1,None,node2)
        test = self.leet94.inorder_traversal(node1)
        self.assertEqual(test, [1,3,2])


if __name__ == "__main__":
    unittest.main()
