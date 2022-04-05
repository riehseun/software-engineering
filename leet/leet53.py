# /usr/bin/env python3.6

# https://leetcode.com/problems/maximum-subarray/

import math


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

        return sum(self.subroutine(nums))


    def subroutine(self, nums):
        """
        Sub-routine to perform divide and conquer algorithm.

        Args:
            nums -- An array of integers.

        Returns:
            contiguous sub-array whose sum of element is the larget.
        """

        if len(nums) == 1:
            return nums

        mid_index = math.trunc(len(nums)/2)

        result_left_half = self.subroutine(nums[:mid_index])
        result_right_half = self.subroutine(nums[mid_index:])
        last_index_left_half = len(result_left_half)-1
        last_index_right_half = mid_index + len(result_right_half)-1
        sum_left_half = sum(result_left_half)
        sum_right_half = sum(result_right_half)
        sum_contiguous = sum(nums[last_index_left_half:last_index_right_half+1])
        # sum_contiguous = sum(result_left_half+result_right_half)

        if sum_left_half > sum_right_half:
            if sum_left_half > sum_contiguous:
                return result_left_half
            else:
                return nums[last_index_left_half:last_index_right_half]
        else:
            if sum_right_half > sum_contiguous:
                return result_right_half
            else:
                return nums[last_index_left_half:last_index_right_half]

        # [-2,1,-3,4,-1,2,1,-5,4]

        # [-2,1,-3,4]

        # [-2,1]
        # [-2] 0
        # [1] 0
        # => [1]

        # [-3,4]
        # => [4]



        # [-1,2,1,-5,4]

