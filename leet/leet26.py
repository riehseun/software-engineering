# /usr/bin/env python3.6

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

import math


class Leet26(object):
    def remove_duplicates(self, nums):
        """
        Remove duplicates from sorted array in-place.
        Assume that, 1 <= nums.length <= 3 * 104

        Args:
            nums -- Sorted array in non-decreasing order.

        Returns:
            Integer representing the number of unique element
        """

        if len(nums) == 1:
            return 1

        inf = math.inf
        rem = nums[0]
        i = 1

        # Loop until duplicates are replaced by "inf".
        while rem != inf and nums[i] != inf:
            if nums[i] == rem:
                del nums[i]
                nums.append(inf)
            else:
                rem = nums[i]
                i = i + 1
                # Break if index reaches the end of array.
                if i >= len(nums):
                    break

        # Count the number of unique elements.
        count = 0
        for i in nums:
            if i == inf:
                break
            else:
                count = count + 1

        return count
