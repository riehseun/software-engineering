# /usr/bin/env python3.6

# https://leetcode.com/problems/symmetric-tree/


class Leet101(object):
    def is_symmetric(self, root):
        """
        Find if tree is symmetric.

        Args:
            root -- TreeNode

        Returns:
            True if tree is symmetric. False otherwise.
        """

        if not root:
            return True

        # Time: O(n) where n is the number of nodes in the tree.
        # Space: O(1)
        return self.subroutine(root.left, root.right)



    def subroutine(self, left, right):
        """
        Subroutine to check if left and right subtrees are symmetric.

        Args:
            left -- TreeNode
            right -- TreeNode

        Returns:
            True if left and right subtrees are symmetric.
            False otherwise.
        """

        if not left and not right:
            return True
        if (not left and right) \
            or (left and not right):
            return False

        if left.val != right.val:
            return False
        else:
            out_pair = self.subroutine(left.left, right.right)
            in_pair = self.subroutine(left.right, right.left)

            # If one of them is False, should return False.
            return out_pair and in_pair
