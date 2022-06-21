# /usr/bin/env python3.6

# https://leetcode.com/problems/3sum-closest/

import math


class Leet16(object):
    def three_sum_closest(self, nums, target):
        """
        Find three integers whose sum is closest to target.

        Args:
            nums -- A list of integers.
            target -- An integer.

        Returns:
            Three integers whose sum is closest to target.
        """

        diff = math.inf
        three_sum = math.inf

        nums.sort()  # O(nlogn)

        # Time: O(n^2)
        # Space: O(1)
        for i in range(len(nums)):
            start = 0
            end = len(nums) - 1
            while start < i and i < end:
                # If the sum is less than target, increment start to increase
                # the sum.
                if nums[i]+nums[start]+nums[end] < target:
                    if abs(nums[i]+nums[start]+nums[end]-target) < diff:
                        diff = abs(nums[i]+nums[start]+nums[end]-target)
                        three_sum = nums[i] + nums[start] + nums[end]
                    start += 1
                else:
                    if abs(nums[i]+nums[start]+nums[end]-target) < diff:
                        diff = abs(nums[i]+nums[start]+nums[end]-target)
                        three_sum = nums[i] + nums[start] + nums[end]
                    end -= 1

        return three_sum