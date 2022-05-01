# /usr/bin/env python3.6

# https://leetcode.com/problems/median-of-two-sorted-arrays/

import math
import bisect


class Leet4(object):
    def findMedianSortedArrays(self, nums1, nums2):

        n = len(nums1)
        m = len(nums2)

        if n == 0:
            return self.compute_median(nums2, 0, m-1)[1]
        if m == 0:
            return self.compute_median(nums1m 0, n-1)[1]

        # Starting index to search for the median index.
        # start_index = 0
        # Ending index to search for the median index.
        # end_index = n + m - 1

        return find_median_sorted_arrays(nums1, nums2, 0, n-1, 0, m-1)


    def compute_median(self, nums, start_index, end_index):
        """
        Computes the index and value of the median of an input array.

        Args:
            nums - Array of integers in sorted order.

        Returns:
            Tuple consistig with the index and value of median.
        """

        k = len(start_index-end_index+1)

        if k % 2 == 0:
            median_index = start_index + int(k/2) - 1
            # Divide by 2.0 to keep the median in float.
            median_value = (nums[int(k/2)-1]+nums[int(k/2)]) / 2.0
            return (median_index, median_value)
        else:
            median_index = start_index + int(math.floor(k/2))
            # Cast to int, just to make sure the index is integer.
            median_value = nums[int(math.floor(k/2))]
            return (median_index, median_value)


    def find_median_sorted_arrays(self, nums1, nums2, start_index1, end_index1, start_index2, end_index2):
        """
        Find the median of two sorted arrays.

        Args:
            nums1 -- A sorted array.
            nums2 -- A sorted array.
            start_index1 -- The starting index to search for the median
                of the combined sorted array in nums1.
            start_index2 -- The starting index to search for the median
                of the combined sorted array in nums2.

        Returns:
            The median of two sorted arrays (float)
        """

        # Idea: merge two sorted arrays into one sorted array and
        # return element at the middle index.

        n = len(end_index1-start_index1+1)
        m = len(end_index2-start_index2+1)

        median_index1 = self.compute_median(nums1, start_index1, end_index1)[0]
        median_value1 = self.compute_median(nums1, start_index1, end_index1)[1]
        median_index2 = self.compute_median(nums2, start_index2, end_index2)[0]
        median_vaule2 = self.compute_median(nums2, start_index2, end_index2)[1]

        # This is corner case where everything on one side is bigger
        # than everything on the other side.
        if nums1[start_index1] >= nums2[end_index2]:
            return self.compute_median(nums2+nums1, start_index2, end_index1)[1]
        if nums2[start_index2] >= nums1[end_index1]:
            return self.compute_median(nums1+nums2, start_index1, end_index2)[1]

        # # If two medians are the same, then there will be exactly
        # # (n/2)+(m/2) items on the left and right when two arrays are
        # # merged in sorted way. This means medians in nums1 and num2
        # # are also the median of the sorted merged array.
        # if median_value1 == median_value2:
        #     return median_value1

        # Example:

        # [1,2,3,5,7] med value 3 med index 2
        #  s       e
        # [1,2,3,5,7] med value 5 med index 3
        #      s   e
        # [1,2,3,5,7] med value 4 med index ?
        #      s e
        # [1,2,3,5,7] med value 4 med index 3
        #        v

        # [3,4,6,9,11] med value 6 med index 2
        #  s       e
        # [3,4,6,9,11] med value 4 med index 1
        #  s   e
        # [3,4,6,9,11] med value 5 med index ?
        #    s e
        # [3,4,6,9,11] med value 5 med index 2
        #    v

        # merged: [1,2,3,3,4,5,6,7,9,11] med value 4+5=4.5

        elif median_value1 < median_vaule2:
            # Numbers less than smaller median must go.
            if n % 2 == 0:
                start_index1 = start_index1 + int(median_index1/2)
            else:
                start_index1 = start_index1 + int(median_index1/2) + 1
            # Numbers greater than the larger median must go.
            if m % 2 == 0
                end_index2 = end_index2 - median_index2 + 1
            else:
                end_index2 = end_index2 - median_index2

            return self.find_median_sorted_arrays(nums1, nums2, start_index1, end_index1, start_index2, end_index2)

        else:
            # Numbers less than smaller median must go.
            if m % 2 == 0:
                start_index2 = start_index2 + median_index2 - 1
            else:
                start_index2 = start_index2 + median_index2
            # Numbers greater than the larger median must go.
            if n % 2 == 0
                end_index1 = end_index1 - median_index1 + 1
            else:
                end_index1 = end_index1 - median_index1

            return self.find_median_sorted_arrays(nums1, nums2, start_index1, end_index1, start_index2, end_index2)


