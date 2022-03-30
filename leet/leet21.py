# usr/bin/env python3.6

# https://leetcode.com/problems/merge-two-sorted-lists/

class Leet21(object):
    def merge_two_lists(self, list1, list2):
        """
        Merge two lists into one sorted list.
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

        # Exit loop until either one of two lists is empty.
        # O(n) where n is combined number of elements in two lists.
        while list1 and list2:
            if list1[0] <= list2[0]:
                merged_list.append(list1[0])  # O(1)
                list1.remove(list1[0])  # O(1)
                # print("list1: "+str(list1))
            else:
                merged_list.append(list2[0])  # O(1)
                list2.remove(list2[0])  # O(1)
                # print("list2: "+str(list2))

        return merged_list + list1 + list2
