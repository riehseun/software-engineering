# /usr/bin/env python3.6

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

import math


class Leet26(object):
    def remove_duplicates(self, nums):
        """
        Remove duplicates from sorted array in-place.
        Assume that, 1 <= len(nums) <= 3 * 104.

        Args:
            nums -- Sorted array in non-decreasing order.

        Returns:
            Integer representing the number of unique element.
        """

        if len(nums) == 1:
            return 1

        inf = math.inf
        rem = nums[0]  # Store the first number.
        i = 1

        # Loop until duplicates are replaced by "inf".
        # Time: O(n) worst case is looping through the entire list.
        # Space: O(1)
        while rem != inf and nums[i] != inf:
            if nums[i] == rem:
                del nums[i]  # Remove duplicate from the list.
                nums.append(inf)  # Add inf to sustain list size.
            else:
                rem = nums[i]  # Move to the next number.
                i = i + 1
                # Break if index reaches the end of array.
                if i >= len(nums):
                    break

        # Count the number of unique elements.
        # Time: O(n).
        # Space: O(1).
        count = 0
        for i in nums:
            if i == inf:
                break
            else:
                count = count + 1

        return count
