# usr/bin/env python3.6

# https://leetcode.com/problems/merge-two-sorted-lists/


class Leet21(object):
    def merge_two_lists(self, list1, list2):
        """
        Merge two lists into a one sorted list.
        Assume list1 and list2 are sorted in non-decreasing order.

        Args:
            list1 -- A list of integers.
            list2 -- A list of integers.

        Returns:
            A sorted list.
        """

        if not list1:
            return list2
        if not list2:
            return list1

        merged_list = []

        # Iterate until either one of two lists is empty.
        # Time: O(n) where n is combined number of elements in the two
        # lists.
        # Space: O(n) worst case is that n-1 can be appeneded to the
        # merged list.
        while list1 and list2:
            if list1[0] <= list2[0]:
                merged_list.append(list1[0])  # O(1)
                list1.remove(list1[0])  # O(1) list1 is sorted list.
            else:
                merged_list.append(list2[0])  # O(1)
                list2.remove(list2[0])  # O(1) list2 is sorted list.

        return merged_list + list1 + list2
