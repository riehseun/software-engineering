# /usr/bin/env python3.6

# https://leetcode.com/problems/remove-element/


class Leet27(object):
    def remove_element(self, nums, val):
        """
        Remove all occurences of val in num in-place.

        Args:
            nums -- An array of integers.
            val -- An integer.
        """

        while val in nums:
            nums.remove(val)

        return len(nums)
