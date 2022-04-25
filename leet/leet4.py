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

        n = len(nums1)
        m = len(nums2)
        # Start and end indexes are possible locations where the median
        # could be.
        start_index = 0
        end_index = n + m - 1

    def find_ith_element(self, nums1, nums2):
        """
        Find ith element from the combined sorted array, which results
        from merging two sorted array (nums1, nums2)

        Args:
            nums1 -- A sorted array.
            nums2 -- A sorted array.

        Returns:
            ith element from the combined sorted array (float)
        """

        # Key idea:
        # 1. numbers less than smaller median of the two array cannot
        # be the median of combined sorted array.
        # 2. The index



        pass


    # def compute_median(self, nums):
    #     """
    #     Computes the median of an input array

    #     Args:
    #         nums - array of integers in sorted order.

    #     Returns:
    #         Median (an integer)
    #     """

    #     n = len(nums)

    #     if n == 1:
    #         return nums[0]

    #     if n % 2 == 0:
    #         # Divide by 2.0 to keep the median in float.
    #         return (nums[int(n/2)-1]+nums[int(n/2)]) / 2.0
    #     else:
    #         # Cast to int, just to make sure the index is integer.
    #         return nums[int(math.floor(n/2))]


    # # This seems to work only when the inputs are positive.

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

    #     n = len(nums1)
    #     m = len(nums2)

    #     if n == 0:
    #         return self.compute_median(nums2)
    #     if m == 0:
    #         return self.compute_median(nums1)

    #     if n == 1 and m == 1:
    #         return (nums1[0]+nums2[0]) / 2.0

    #     median_nums1 = self.compute_median(nums1)
    #     median_nums2 = self.compute_median(nums2)

    #     # This is corner case where everything on one side is bigger
    #     # than everything on the other side.
    #     if nums1[len(nums1)-1] <= nums2[0]:
    #         return self.compute_median(nums1+nums2)
    #     if nums2[len(nums2)-1] <= nums1[0]:
    #         return self.compute_median(nums2+nums1)

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
    #     # 4.5 lies between 3 and 6
    #     # All values less than 3 or greater than 6 will not be the
    #     # median of the merged array.
    #     elif median_nums1 < median_nums2:
    #         # Numbers less than smaller median must go.
    #         right_half = nums1[int(math.floor(n/2)):]
    #         # if n % 2 == 0:
    #         #     right_half = nums1[math.floor(n/2):]
    #         #     left_half = nums2[:m-math.floor(n/2)]
    #         # else:
    #         #     right_half = nums1[math.floor(n/2)+1:]
    #         #     left_half = nums2[:m-math.floor(n/2)-1]
    #         # print(right_half)
    #         # print(left_half)
    #         if nums1[int(math.floor(n/2))] > nums2[int(math.floor(m/2))]:
    #             return median_nums2
    #         else:
    #             left_half = nums2[:m-int(math.floor(n/2))]
    #             print(left_half)
    #             return self.find_median_sorted_arrays(right_half,left_half)

    #     # Example:
    #     # nums1: [3,4,6,9,11] med 6
    #     # nums2: [1,2,3,5,7] med 3
    #     # merged: [1,2,3,3,4,5,6,7,9,11] med is (4+5)/2=4.5
    #     # 4.5 lies between 6 and 3
    #     # All values greater than 6 or less than 3 will not be the
    #     # median of the merged array.
    #     else:
    #         # Numbers less than smaller median must go.
    #         right_half = nums2[int(math.floor(m/2)):]
    #         # if m % 2 == 0:
    #         #     right_half = nums2[math.floor(m/2):]
    #         #     left_half = nums1[:n-math.floor(m/2)]
    #         # else:
    #         #     right_half = nums2[math.floor(m/2)+1:]
    #         #     left_half = nums1[:n-math.floor(m/2)]
    #         # print(right_half)
    #         # print(left_half)
    #         if nums2[int(math.floor(m/2))] > nums1[int(math.floor(n/2))]:
    #             return median_nums1
    #         else:
    #             left_half = nums1[:n-int(math.floor(m/2))]
    #             return self.find_median_sorted_arrays(left_half,right_half)

