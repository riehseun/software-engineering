# /usr/bin/env python3.6

# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Leet297(object):
    def serialize(self, root):
        """
        Encodes a tree into a representation.

        Args:
            root -- TreeNode.

        Returns:
            Encoded representation in tuple.
        """

        if root is None:
            return "null"

        #      1
        #   2     3
        #       4   5
        # root = [1,2,3,null,null,4,5]
        # ('1', ('2', 'null', 'null'), ('3', ('4', 'null', 'null'),
        # ('5', 'null', 'null')))
        return str(root.val), \
            self.serialize(root.left), \
            self.serialize(root.right)


    def deserialize(self, data):
        """
        Decodes the encoded data to tree.

        Args:
            data -- Encoded representation in tuple.

        Returns:
            TreeNode.
        """

        if data == "null":
            return None

        node = TreeNode(data[0])
        node.left = self.deserialize(data[1])
        node.right = self.deserialize(data[2])

        return node
