# usr/bin/env python3.6

# https://leetcode.com/problems/merge-two-sorted-lists/


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Leet21(object):
    def merge_two_lists(self, list1, list2):
        """
        Merge two linked lists into a one sorted linked list.
        Assume list1 and list2 are sorted in non-decreasing order.

        Args:
            list1 -- A linked list of integers.
            list2 -- A linked list of integers.

        Returns:
            A sorted linked list.
        """

        # Example: [1,2,4], [1,3,4] => [1,1,2,3,4,4]

        list3 = ListNode()
        temp = list3

        # Time: O(n) where n is the combined lenght of two linked lists.
        # Space: O(1) no additional space allocated.
        while list1 and list2:
            if list1.val < list2.val:
                print(list1.val)
                list3.next = list1
                list1 = list1.next
            else:
                print(list2.val)
                list3.next = list2
                list2 = list2.next
            list3 = list3.next

        if list1:
            print(list1.val)
            list3.next = list1
        if list2:
            print(list2.val)
            list3.next = list2

        # Returning list3.next will return the last node in the linked
        # list we computed. To return the first node, we use temp.
        return temp.next