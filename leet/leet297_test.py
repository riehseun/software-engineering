import unittest

from leet297 import Leet297


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestLeet297(unittest.TestCase):
    def setUp(self):
        self.leet297 = Leet297()

    def test_serialize_1(self):
        node4 = TreeNode(5,None,None)
        node3 = TreeNode(4,None,None)
        node2 = TreeNode(3,node3,node4)
        node1 = TreeNode(2,None,None)
        root = TreeNode(1,node1,node2)
        encoded_tuple = self.leet297.serialize(root)
        print(encoded_tuple)
        test = self.leet297.deserialize(encoded_tuple)
        print(test)
        self.assertEqual(test.val, root.val)


if __name__ == "__main__":
    unittest.main()
