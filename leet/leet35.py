# /usr/bin/env python3.6

# https://leetcode.com/problems/search-insert-position/

import math


class Leet35(object):
    def search_insert(self, nums, target):
        """
        Find the insert position in the array for the target number.

        Args:
            nums -- Sorted array of distinct integers.
            target -- An integer.

        Returns:
            Index if target is in array. Insert position (index)
            otherwise.
        """

        # If target is bigger than even the biggest number in nums.
        if target > nums[len(nums)-1]:
            return len(nums)  # O(1)

        # Time: O(n).
        # Space: O(1).
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
