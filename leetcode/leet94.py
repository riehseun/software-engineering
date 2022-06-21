# /usr/bin/env python3.6

# https://leetcode.com/problems/binary-tree-inorder-traversal/


class Leet94(object):
    def inorder_traversal(self, root):
        """
        Finds node values in inorder traversal.
        This is DFS where Left -> Node -> Right

        Args:
            root - TreeNode

        Returns:
            An array with inorder traversal result.

        """

        # Example:
        #    1
        #        2
        #      3
        # [None, None, None, 1, 3, 2, None]

        if not root:
            return []

        return self.inorder_traversal(root.left) \
            + [root.val] \
            + self.inorder_traversal(root.right)


