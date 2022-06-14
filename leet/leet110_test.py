import unittest

from leet110 import Leet110
from treenode import TreeNode


class TestLeet110(unittest.TestCase):
    def setUp(self):
        self.leet110 = Leet110()

    def test_is_balanced_1(self):
        node5 = TreeNode(7,None,None)
        node4 = TreeNode(15,None,None)
        node3 = TreeNode(20,node4,node5)
        node2 = TreeNode(9,None,None)
        node1 = TreeNode(3,node2,node3)
        test = self.leet110.is_balanced(node1)
        self.assertEqual(test, True)


if __name__ == "__main__":
    unittest.main()
