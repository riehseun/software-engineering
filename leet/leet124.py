# /usr/bin/env python3.6

# https://leetcode.com/problems/binary-tree-maximum-path-sum/


class Leet124(object):
    def max_path_sum(self, root):
        """
        Find the maximum possible sum of nodes' value in any path in a
        tree.

        Args:
            root -- TreeNode object.

        Returns:
            The maximum possible sum.
        """

        # Questions:
        # Can a node have a negative number? yes
        # Will a node have non-integer values? no
        # Is the tree balanced tree? Not necessariliy
        # Is the tree binary tree? Not necessariliy

        # Key idea: for each node, find the path that leads to the max
        # value while at the same time keeping track of tje maximum
        # possible sum of connected nodes from that node.

        # Time: O(h) where h is the height of the tree.
        # Space: O(n) where n is the number of nodes.
        max_sum = []
        self.subroutine(root, max_sum)
        return max(max_sum)


    def subroutine(self, node, max_sum):
        """
        Subroutine to solve max_path_sum problem.

        Args:
            node -- TreeNode object.
            max_sum -- maximum possible sum computed so far.

        Returns:
            The maximum possible sum.
        """

        # Example:
        #   -10
        #  9    20
        #     15   7
        #
        #   -10
        #  9    42

        if node is None:
            return 0

        sum_from_left_subtree = max(self.subroutine(node.left, max_sum), 0)
        sum_from_right_subtree = max(self.subroutine(node.right, max_sum), 0)

        # At each node, the maximum sum can be constructed by.
        max_sum.append(node.val+sum_from_left_subtree+sum_from_right_subtree)

        # At each node, the path can only be constructed by taking
        # either one of left or right child node.
        max_path = node.val + max(sum_from_left_subtree, sum_from_right_subtree)
        return max_path

