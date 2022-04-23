# /usr/bin/env python3.6

# https://leetcode.com/problems/median-of-two-sorted-arrays/

import math


class Leet4(object):
    def find_median_sorted_arrays(self, nums1, nums2):
        """
        Find the median of two sorted arrays.

        Args:
            nums1 -- A sorted array.
            nums2 -- A sorted array.

        Returns:
            The median of two sorted arrays (float)
        """

        # Idea:


    # This seems to work only when the inputs are positive.

    # def find_median_sorted_arrays(self, nums1, nums2):
    #     """
    #     Find the median of two sorted arrays.

    #     Args:
    #         nums1 -- A sorted array.
    #         nums2 -- A sorted array.

    #     Returns:
    #         The median of two sorted arrays (float)
    #     """

    #     # Idea: merge two sorted arrays into one sorted array and
    #     # return element at the middle index.

    #     if len(nums1) == 1 and len(nums2) == 1:
    #         return (nums1[0]+nums2[0])/2.0

    #     n = len(nums1)
    #     m = len(nums2)

    #     if n == 1:
    #         median_nums1 = nums1[0]
    #     if n > 1:
    #         if n % 2 == 0:
    #             # Divide by 2.0 to keep the median in float.
    #             median_nums1 = (nums1[int(n/2)-1]+nums1[int(n/2)]) / 2.0
    #         else:
    #             # Cast to int, just to make sure the index is integer.
    #             median_nums1 = nums1[int(math.floor(n/2))]

    #     if m == 1:
    #         median_nums2 = nums2[0]
    #     if m > 1:
    #         if m % 2 == 0:
    #             median_nums2 = (nums2[int(m/2)-1]+nums2[int(m/2)]) / 2.0
    #         else:
    #             median_nums2 = nums2[int(math.floor(m/2))]

    #     if n == 0:
    #         return median_nums2
    #     if m == 0:
    #         return median_nums1

    #     # If two medians are the same, then there will be exactly
    #     # (n/2)+(m/2) items on the left and right when two arrays are
    #     # merged in sorted way. This means medians in nums1 and num2
    #     # are also the median of the sorted merged array.
    #     if median_nums1 == median_nums2:
    #         return median_nums1

    #     # Example:
    #     # nums1: [1,2,3,5,7] med 3
    #     # nums2: [3,4,6,9,11] med 6
    #     # merged: [1,2,3,3,4,5,6,7,9,11] med is (4+5)/2=4.5
    #     # The median exists in right half of (n/2) and the left half of
    #     # (m/2) [5,7] and [3,4]
    #     elif median_nums1 < median_nums2:
    #         if n % 2 == 0:
    #             right_half = nums1[int(n/2):]
    #         else:
    #             right_half = nums1[int(n/2)+1:]
    #         left_half = nums2[:int(m/2)]
    #         return self.find_median_sorted_arrays(right_half,left_half)

    #     # Example:
    #     # nums1: [3,4,6,9,11] med 6
    #     # nums2: [1,2,3,5,7] med 3
    #     # merged: [1,2,3,3,4,5,6,7,9,11] med is (4+5)/2=4.5
    #     # The median exists in left half of (n/2) and the right half of
    #     # (m/2) [3,4] and [5,7]
    #     else:
    #         left_half = nums1[:int(n/2)]
    #         if m % 2 == 0:
    #             right_half = nums2[int(m/2):]
    #         else:
    #             right_half = nums2[int(m/2)+1:]
    #         return self.find_median_sorted_arrays(left_half,right_half)
