# /usr/bin/env python3.6

# https://leetcode.com/problems/median-of-two-sorted-arrays/

import math
import bisect


class Leet4(object):
    def find_median_sorted_arrays(self, nums1, nums2):

        n = len(nums1)
        m = len(nums2)

        # when total length is odd, the median is the middle
        if (n+m) % 2 != 0:
            return self.find_ith_element(nums1, 0, n-1, nums2, 0, m-1, int((n+m)/2))
        else:
        # when total length is even, the median is the average of the middle 2
            middle1 = self.find_ith_element(nums1, 0, n-1, nums2, 0, m-1, int((n+m)/2))
            middle2 = self.find_ith_element(nums1, 0, n-1, nums2, 0, m-1, int((n+m)/2)-1)
            return (middle1 + middle2) / 2.0

        # if n == 0:
        #     return nums2[int(m/2)]
        # if m == 0:
        #     return nums1[int(n/2)]


    def find_ith_element(self, nums1, start1, end1, nums2, start2, end2, i):
        """
        Find the median of two sorted arrays.

        Args:
            nums1 -- A sorted array.
            start1 -- The starting index to search for the median
                of the combined sorted array in nums1.
            end1 -- The ending index to search for the median
                of the combined sorted array in nums1.
            nums2 -- A sorted array.
            start2 -- The starting index to search for the median
                of the combined sorted array in nums2.
            end2 -- The ending index to search for the median
                of the combined sorted array in nums2.
            i -- ith element to find.

        Returns:
            The median of merged sorted arrays (float)
        """

        # Idea: merge two sorted arrays into one sorted array and
        # return element at the middle index.

        # Example #1:
        # [1,2,3,5,7] and [3,4,6,9,11]
        # Merged: [1,2,3,3,4,5,6,7,9,11]

        # [1,2,3,5,7] [3,4,6,9,11] i=5, 2+2=4 < 5
        #  s       e   s       e

        # [1,2,3,5,7] [3,4,6,9,11] i=5, 3+1=4 < 5
        #      s   e   s   e

        # [1,2,3,5,7] [3,4,6,9,11] i=5, 2+1=3 < 5
        #      s e       s e

        # [1,2,3,5,7] [3,4,6,9,11] i=5, 2+1=3 < 5
        #        v       v

        # [1,2,3,5,7] [3,4,6,9,11] i-start1=5-4=1, nums2[1]=4
        #                x

        # Example #2:
        # [2,7] and [1,3,4,5,6]
        # Merged: [1,2,3,4,5,6,7]

        # [2,7] [1,3,4,5,6] i=4, 0+2 < 4
        #  s e   s       e

        # [2,7] [1,3,4,5,6] i=4, 0+3 < 4
        #  s e       s   e

        # [2,7] [1,3,4,5,6] i-start1=4-1=3, nums2[]
        #    v       s   e

        # [2,7] [1,3,4,5,6] i=4, 1+3 == 4
        #    v       s   e

        if start1 > end1:
            return nums2[i-start1]
        if start2 > end2:
            return nums1[i-start2]

        mid1 = int((start1+end1)/2)
        mid2 = int((start2+end2)/2)
        mid1_val = nums1[mid1]
        mid2_val = nums2[mid2]

        if mid1 + mid2 < i:
            # Median exists greater or equal than the smaller median and
            # lesser or equal than the larger median.
            if mid1_val < mid1_val:
                return self.find_ith_element(nums1, mid1, end1, nums2, start2, mid2, i)
            else:
                return self.find_ith_element(nums1, start1, mid1, nums2, mid2, end2, i)
        else:
            if mid1_val < mid2_val:
                return self.find_ith_element(nums1, start1, end1, nums2, mid2, end2, i)
            else:
                return self.find_ith_element(nums1, mid1, end1, nums2, start2, mid2, i)



