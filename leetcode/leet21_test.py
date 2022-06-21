import unittest

from leet21 import Leet21, ListNode


class TestLeet21(unittest.TestCase):
    def setUp(self):
        self.leet21 = Leet21()

    def test_merge_two_lists_1(self):
        node12 = ListNode(4, None)
        node11 = ListNode(4, node12)
        node10 = ListNode(3, node11)
        node9 = ListNode(2, node10)
        node8 = ListNode(1, node9)
        node7 = ListNode(1, node8)
        node6 = ListNode(4, None)
        node5 = ListNode(3, node6)
        node4 = ListNode(1, node5)
        node3 = ListNode(4, None)
        node2 = ListNode(2, node3)
        node1 = ListNode(1, node2)
        test = self.leet21.merge_two_lists(node1, node4)
        print("-----")
        while test:
            print(test.val)
            test = test.next
        self.assertEqual(test.val, node7.val)


if __name__ == "__main__":
    unittest.main()