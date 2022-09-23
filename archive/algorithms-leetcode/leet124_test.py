import unittest

from leet124 import Leet124


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestLeet124(unittest.TestCase):
    def setUp(self):
        self.leet124 = Leet124()

    def test_max_path_sum_1(self):
        node2 = TreeNode(3,None,None)
        node1 = TreeNode(2,None,None)
        root = TreeNode(1,node1,node2)
        test = self.leet124.max_path_sum(root)
        self.assertEqual(test, 6)

    def test_max_path_sum_2(self):
        node4 = TreeNode(7,None,None)
        node3 = TreeNode(15,None,None)
        node2 = TreeNode(20,node3,node4)
        node1 = TreeNode(9,None,None)
        root = TreeNode(-10,node1,node2)
        test = self.leet124.max_path_sum(root)
        self.assertEqual(test, 42)

    def test_max_path_sum_3(self):
        root = TreeNode(-3,None,None)
        test = self.leet124.max_path_sum(root)
        self.assertEqual(test, -3)

    def test_max_path_sum_4(self):
        node1 = TreeNode(-1,None,None)
        root = TreeNode(-2,node1,None)
        test = self.leet124.max_path_sum(root)
        self.assertEqual(test, -1)

    def test_max_path_sum_5(self):
        node2 = TreeNode(-3,None,None)
        node1 = TreeNode(-1,node2,None)
        root = TreeNode(-2,node1,None)
        test = self.leet124.max_path_sum(root)
        self.assertEqual(test, -1)

    def test_max_path_sum_6(self):
        node2 = TreeNode(1,None,None)
        node1 = TreeNode(-1,node2,None)
        root = TreeNode(-2,node1,None)
        test = self.leet124.max_path_sum(root)
        self.assertEqual(test, 1)

    def test_max_path_sum_7(self):
        node6 = TreeNode(-1,None,None)
        node5 = TreeNode(-2,None,None)
        node4 = TreeNode(3,None,None)
        node3 = TreeNode(1,node6,None)
        node2 = TreeNode(-3,node5,None)
        node1 = TreeNode(-2,node3,node4)
        root = TreeNode(1,node1,node2)
        test = self.leet124.max_path_sum(root)
        self.assertEqual(test, 3)


if __name__ == "__main__":
    unittest.main()
