# /usr/bin/env python3.6

# https://leetcode.com/problems/merge-sorted-array/


class Leet88(object):
    def merge(self, nums1, m, nums2, n):
        """
        Merge two sorted arrays into one sorted array.

        Args:
            nums1 -- A sorted array in non-decreasing order.
            nums2 -- A sorted array in non-decreasing order.
            m -- Length of nums1.
            n -- Length of nums2.

        Returns:
            nums1 which is the sorted array combining nums1 and nums2.
        """

        # Example: [2,0], 1, [1], 1
        # [2,0] m=1 n=1
        # [2,2] m=0 n=1
        # n > 0 => [1,2]

        if n == 0:
            return nums1
        if m == 0:
            for i in range(len(nums2)):
                nums1[i] = nums2[i]
            return nums1

        # Time: O(m+n)
        # Space: O(1)
        while n > 0 and m > 0:
            if nums2[n-1] > nums1[m-1]:
                nums1[n+m-1] = nums2[n-1]
                n -= 1
            else:
                nums1[n+m-1] = nums1[m-1]
                m -= 1

        if n > 0:
            nums1[:n] = nums2[:n]

        return nums1

