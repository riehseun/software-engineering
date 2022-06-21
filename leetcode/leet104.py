# /usr/bin/env python3.6

# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/


class Leet104(object):
    def max_depth(self, root):
        """
        Finds the max depth of a binary tree.

        Args:
            root -- TreeNode

        Returns:
            The max depth of a binary tree.
        """

        if not root:
            return 0

        # Time: O(n) where n is the number of nodes.
        # Space: O(1)
        return self.subroutine(root, 0)


    def subroutine(self, node, depth):
        """
        Find the max depth of two subtrees of a node.

        Args:
            node -- TreeNode
            max_depth -- keeps track of max depth

        Returns:
            The maximum depth.
        """

        if not node:
            return depth

        # Each time the recursive call is made, increase the depth by 1.
        return max(self.subroutine(node.left, depth+1), \
            self.subroutine(node.right, depth+1))



