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

        # Time: O(n) although while loop and remove operation are both
        # O(n), the total operation cannot exceed the length of list.
        while val in nums:
            nums.remove(val)  # O(n)

        return len(nums)
