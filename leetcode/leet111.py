# /usr/bin/env python3.6

# https://leetcode.com/problems/minimum-depth-of-binary-tree/

from treenode import TreeNode


class Leet111(object):
    def min_depth(self, root):
        """
        Find the minimum depth of a tree.

        Args:
            root -- TreeNode.

        Returns:
            Minimum depth of a tree.
        """

        if not root:
            return 0

        # Time: O(n) where n is the number of nodes.
        # Space: O(1)
        return self.subroutine(root, 0)


    def subroutine(self, node, depth):
        """
        Find the min depth of two subtrees of a node.

        Args:
            node -- TreeNode
            min_depth -- keeps track of max depth

        Returns:
            The minimum depth.
        """

        if not node:
            return depth

        # Each time the recursive call is made, increase the depth by 1.
        return min(self.subroutine(node.left, depth+1), \
            self.subroutine(node.right, depth+1))
