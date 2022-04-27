# /usr/bin/env python3.6

# https://leetcode.com/problems/median-of-two-sorted-arrays/

import math
import bisect


class Leet4(object):
    # def find_median_sorted_arrays(self, nums1, nums2):
    #     """
    #     Find the median of two sorted arrays.

    #     Args:
    #         nums1 -- A sorted array.
    #         nums2 -- A sorted array.

    #     Returns:
    #         The median of two sorted arrays (float)
    #     """


    #     # if (n+m) % 2 == 0:
    #     #     median_left_index = int((math.floor((n+m-1)/2))/2)
    #     #     median_right_index = int((math.floor((n+m-1)/2))/2)
    #     #     return (self.find_ith_element(nums1, 0, nums2, 0, median_left_index) \
    #     #         + self.find_ith_element(nums1, 0, nums2, 0, median_right_index)) \
    #     #         / 2.0
    #     # else:
    #     #     median_index = int((n+m-1)/2)
    #     #     return self.find_ith_element(nums1, 0, nums2, 0, median_index)

    #     n = len(nums1)
    #     m = len(nums2)
    #     l = math.floor((m+n+1)/2)
    #     r = math.ceil((m+n+1)/2)
    #     return (self.find_ith_element(nums1, 0, nums2, 0, l-1) \
    #         + self.find_ith_element(nums1, 0, nums2, 0, r-1)) / 2.0


    # def find_median_element(self, nums1, start_index1, nums2, start_index2):
    #     """
    #     Find ith element from the combined sorted array, which results
    #     from merging two sorted arrays. (nums1, nums2)

    #     Args:
    #         nums1 -- A sorted array.
    #         start_index1 -- Index to begin the search from in nums1.
    #         nums2 -- A sorted array.
    #         start_index2 -- Index to begin the search from in nums2.
    #         i -- Index of the combined sorted array.

    #     Returns:
    #         ith element from the combined sorted array. (float)
    #     """

    #     # Key idea:
    #     # 1. Numbers less than smaller median of the two array cannot
    #     # be the median of the combined sorted array.

    #     # Example:
    #     # nums1: [1,2,3,5,7] start index 0
    #     # nums2: [3,4,6,9,11] start index 0
    #     # merged: [1,2,3,3,4,5,6,7,9,11] find 5th and 6th, which are 4,5

    #     # Example:
    #     # nums1: [1,3] start_index1 0
    #     # nums2: [2] start_index2 0
    #     # merged: [1,2,3] i = 1

    #     if start_index1 > len(nums1) - 1:
    #         return nums2[int(start_index2+i)]
    #     if start_index2 > len(nums2) - 1:
    #         return nums1[int(start_index1+i)]

    #     # First item in the combined sorted array will be smaller item
    #     # of the two sorted arrays.
    #     if i == 0:
    #         return min(nums1[start_index1], nums2[start_index2])

    #     median_1 = math.inf;
    #     median_2 = math.inf;
    #     if start_index1 + i/2 < len(nums1):
    #         median_1 = nums1[int(start_index1+i/2)]
    #     if start_index2 + i/2 < len(nums2):
    #         median_2 = nums2[int(start_index2+i/2)]

    #     if median_1 == median_2:
    #         return median_1
    #     elif median_1 < median_2:
    #         return self.find_median_element(
    #             nums1, start_index1+i/2, nums2, start_index2, i-i/2)
    #     else:
    #         return self.find_median_element(
    #             nums1, start_index1, nums2, start_index2+i/2, i-i/2)


    def compute_median(self, nums):
        """
        Computes the median of an input array

        Args:
            nums - array of integers in sorted order.

        Returns:
            Median (an integer)
        """

        n = len(nums)

        if n == 1:
            return nums[0]

        if n % 2 == 0:
            # Divide by 2.0 to keep the median in float.
            return (nums[int(n/2)-1]+nums[int(n/2)]) / 2.0
        else:
            # Cast to int, just to make sure the index is integer.
            return nums[int(math.floor(n/2))]


    # This seems to work only when the inputs are positive.

    def find_median_sorted_arrays(self, nums1, nums2):
        """
        Find the median of two sorted arrays.

        Args:
            nums1 -- A sorted array.
            nums2 -- A sorted array.

        Returns:
            The median of two sorted arrays (float)
        """

        # Idea: merge two sorted arrays into one sorted array and
        # return element at the middle index.

        n = len(nums1)
        m = len(nums2)

        if n == 0:
            return self.compute_median(nums2)
        if m == 0:
            return self.compute_median(nums1)

        if n == 1:
            if m == 1:
                return (nums1[0]+nums2[0]) / 2.0
            else:
                bisect.insort(nums2, nums1[0])
                return self.compute_median(nums2)

        if m == 1:
            if n == 1:
                return (nums1[0]+nums2[0]) / 2.0
            else:
                bisect.insort(nums1, nums2[0])
                return self.compute_median(nums1)

        if n == 2 and m == 2:
            merged = nums1 + nums2
            merged.sort()
            return (merged[1]+merged[2]) / 2.0

        median_nums1 = self.compute_median(nums1)
        median_nums2 = self.compute_median(nums2)

        # This is corner case where everything on one side is bigger
        # than everything on the other side.
        if nums1[len(nums1)-1] <= nums2[0]:
            return self.compute_median(nums1+nums2)
        if nums2[len(nums2)-1] <= nums1[0]:
            return self.compute_median(nums2+nums1)

        # If two medians are the same, then there will be exactly
        # (n/2)+(m/2) items on the left and right when two arrays are
        # merged in sorted way. This means medians in nums1 and num2
        # are also the median of the sorted merged array.
        if median_nums1 == median_nums2:
            return median_nums1
        # Example:
        # nums1: [1,2,3,5,7] med 3
        # nums2: [3,4,6,9,11] med 6
        # merged: [1,2,3,3,4,5,6,7,9,11] med is (4+5)/2=4.5
        # 4.5 lies between 3 and 6
        # All values less than 3 or greater than 6 will not be the
        # median of the merged array.
        elif median_nums1 < median_nums2:
            # Numbers less than smaller median must go.
            nums1_trimmed = nums1[int(math.floor(n/2)):]
            # Numbers greater than the larger median must go.
            nums2_trimmed = nums2[:m-int(math.floor(m/2))]

            nums_removed_from_nums2 = len(nums2) - len(nums2_trimmed)
            nums_removed_from_nums1 = len(nums1) - len(nums1_trimmed)
            diff = abs(nums_removed_from_nums2-nums_removed_from_nums1)

            return self.find_median_sorted_arrays(nums2_trimmed, nums1_trimmed+[math.inf]*diff)

        # Example:
        # nums1: [3,4,6,9,11] med 6
        # nums2: [1,2,3,5,7] med 3
        # merged: [1,2,3,3,4,5,6,7,9,11] med is (4+5)/2=4.5
        # 4.5 lies between 6 and 3
        # All values greater than 6 or less than 3 will not be the
        # median of the merged array.
        else:
            # Numbers less than smaller median must go.
            nums2_trimmed = nums2[int(math.floor(m/2)):]
            # Numbers greater than the larger median must go.
            nums1_trimmed = nums1[:n-int(math.floor(n/2))]

            nums_removed_from_nums2 = len(nums2) - len(nums2_trimmed)
            nums_removed_from_nums1 = len(nums1) - len(nums1_trimmed)
            diff = abs(nums_removed_from_nums2-nums_removed_from_nums1)

            return self.find_median_sorted_arrays(nums1_trimmed, nums2_trimmed+[math.inf]*diff)


