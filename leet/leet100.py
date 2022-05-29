# /usr/bin/env python3.6

# https://leetcode.com/problems/same-tree/


class Leet100(object):
    def is_same_tree(self, p, q):
        """
        Checks if two trees are the same or not.

        Args:
            p - TreeNode
            q - TreeNode

        Returns:
            True if p and q are the same tree. False otherwise.
        """

        # Key idea: Do BFS.
        # Time: O(n) where n is the larger number of nodes in p or q.
        # Space: O(1)
        if not p and not q:
            return True
        if (not p and q) \
            or (p and not q):
            return False

        if p.val != q.val:
            return False

        # If one of them is False, must return False.
        return self.is_same_tree(p.left, q.left) \
            and self.is_same_tree(p.right, q.right)

        return True

