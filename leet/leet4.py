# /usr/bin/env python3.6

# https://leetcode.com/problems/median-of-two-sorted-arrays/

import math
import bisect


class Leet4(object):
    def find_median_sorted_arrays(self, nums1, nums2):
        """
        Find the median element of two sorted arrays.

        Args:
            nums1 -- A sorted array.
            nums2 -- A sorted array.

        Returns:
            The median of merged sorted arrays (float)
        """

        n = len(nums1)
        m = len(nums2)

        l = int((m+n+1)/2)
        r = int((m+n+2)/2)
        return (self.find_ith_element(nums1, 0, nums2, 0, l) \
            + self.find_ith_element(nums1, 0, nums2, 0, r)) / 2.0


    def find_ith_element(self, nums1, start1, nums2, start2, i):
        """
        Find ith element of two sorted arrays.

        Args:
            nums1 -- A sorted array.
            start1 -- The starting index to search for the median
                of the combined sorted array in nums1.
            nums2 -- A sorted array.
            start2 -- The starting index to search for the median
                of the combined sorted array in nums2.
            i -- ith element to find.

        Returns:
            The ith element of merged sorted arrays (float)
        """

        # Median cannot exists in numbers smaller than or equal to
        # the smaller median.

        # Example #1:
        # [1,2,3,5,7] and [3,4,6,9,11] and i=5
        # Merged: [1,2,3,3,4,5,6,7,9,11]

        # [1,2,3,5,7] [3,4,6,9,11] i=5
        #  s           s
        # mid1 = nums1[0+2-1=1] = 2
        # mid2 = nums2[0+2-1=1] = 4

        # [1,2,3,5,7] [3,4,6,9,11] i=3 (discarded 2 items)
        #      s       s
        # mid1 = nums1[2+1-1=2] = 3
        # mid2 = nums2[0+1-1=0] = 3

        # [1,2,3,5,7] [3,4,6,9,11] i=2 (discarded 1 item)
        #      s         s
        # mid1 = nums1[2+1-1=2] = 3
        # mid2 = nums2[1+1-1=1] = 4

        # [1,2,3,5,7] [3,4,6,9,11] i=1
        #        s       s
        # min(5,4) = 4

        # Example #2:
        # [1,3] and [2] and i=2
        # merged: [1,2,3]

        # [1,3] [2] i=2
        #  s     s
        # mid1 = nums1[0+1-1=0] = 1
        # mid2 = nums2[0+1-1=0] = 2

        # [1,3] [2] i=1 (discarded 1 item)
        #    s   s
        # min(3,2) = 2

        n = len(nums1)
        m = len(nums2)

        # If all items are discarded from either one of the arrays, it
        # means that array cannot contain the ith element (since all
        # items are smaller than i). In that case, return ith item
        # from the other array.
        if start1 > n-1:
            return nums2[start2+i-1]
        if start2 > m-1:
            return nums1[start1+i-1]

        if i == 1:
            return min(nums1[start1], nums2[start2])

        mid1 = math.inf
        mid2 = math.inf
        if start1+i/2-1 < n:
            mid1 = nums1[start1+int(i/2)-1]
        if start2+i/2-1 < m:
            mid2 = nums2[start2+int(i/2)-1]

        # Time: O(log(n+m)). We are rejecting i/2 element in each
        # recursive tree.
        # Space: O(1). Not allocating any extra space proportional to
        # input size.
        if mid1 < mid2:
            # We are rejecting elements that are less than smaller
            # median. We are adjusting i to find the original ith
            # element accordingly.
            return self.find_ith_element(
                nums1, start1+int(i/2), nums2, start2, i-int(i/2))
        else:
            return self.find_ith_element(
                nums1, start1, nums2, start2+int(i/2), i-int(i/2))
