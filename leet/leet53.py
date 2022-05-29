# /usr/bin/env python3.6

# https://leetcode.com/problems/maximum-subarray/


class Leet53(object):
    def max_sub_array(self, nums):
        """
        Find contiguous sub-array where the sum of its element is the
        largest.

        Args:
            nums -- An array of integers.

        Returns:
            The largest possible sum of contiguous sub-array of nums.
        """

        # Example: [-2,1,-3,4,-1,2,1,-5,4]
        # [-2,1,-3,4,-1,2,1,-5,4]
        # [-2,1,-3,4,-1,2,1,-5,4] i=1
        # [-2,1,-2,4,-1,2,1,-5,4] i=2
        # [-2,1,-2,4,-1,2,1,-5,4] i=3
        # [-2,1,-2,4, 3,2,1,-5,4] i=4
        # [-2,1,-2,4, 3,5,1,-5,4] i=5
        # [-2,1,-2,4, 3,5,6,-5,4] i=6
        # [-2,1,-2,4, 3,5,6, 1,4] i=7
        # [-2,1,-2,4, 3,5,6, 1,5] i=8

        if len(nums) == 1:
            return sum(nums)

        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]

        return max(nums)

