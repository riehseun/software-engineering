# /usr/bin/env python3.6

# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

from treenode import TreeNode


class Leet108(object):
    def sorted_array_to_bst(self, nums):
        """
        Converted an array of nums into a tree.

        Args:
            nums -- An array of nums sorted in ascending order.

        Returns:
            TreeNode
        """

        # Time: O(n) where n is the number of items in the list.
        # Space: O(1)
        if not nums:
            return None

        n = len(nums)

        if n % 2 == 0:
            mid = int(n/2) - 1
        else:
            mid = int(n/2)

        node = TreeNode(nums[mid])
        node.left = self.sorted_array_to_bst(nums[:mid])
        node.right = self.sorted_array_to_bst(nums[mid+1:])

        return node
