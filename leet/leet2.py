# /usr/bin/env python3.6

# https://leetcode.com/problems/add-two-numbers/


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Leet2(object):
    def add_two_numbers(self, l1, l2):
        """
        Add two numbers whose digits are stored in linked lists.

        Args:
            l1 -- A non-empty linked list.
            l2 -- A non-empty linked list.

        Returns:
            A linked list which computes the sum of two numbers
            represented by l1 and l2.
        """

        # Example: 342 + 465 = 807
        # L1: 2 -> 4 -> 3
        # L2: 5 -> 6 -> 4
        # L3: 7 -> 0 -> 8

        node = ListNode(l1.val+l2.val, None)

        add_two_numbers(l1.next, l2.next)

        return node







