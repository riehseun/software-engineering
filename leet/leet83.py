# /usr/bin/env python3.6

# https://leetcode.com/problems/remove-duplicates-from-sorted-list/


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Leet83(object):
    def delete_duplicates(self, head):
        """
        Delete duplicates from a linked list.

        Args:
            head -- TreeNode

        Returns:
            Linked list with duplicates removed.
        """

        if not head:
            return None

        seen = []
        seen.append(head.val)
        # The head will be at the end of linked list after the interation, so
        # need to store the initial pointer at temp.
        temp = head

        # Time: O(n) where n is number of nodes in linked lists.
        # Space: O(1)
        while head.next:
            if head.next.val not in seen:
                seen.append(head.next.val)
                head = head.next
            else:
                head.next = head.next.next

        return temp

