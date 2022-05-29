import unittest

from leet83 import Leet83, ListNode


class TestLeet83(unittest.TestCase):
    def setUp(self):
        self.leet83 = Leet83()

    def test_delete_duplicates_1(self):
        node3 = ListNode(2, None)
        node2 = ListNode(1, node3)
        node1 = ListNode(1, node2)
        test = self.leet83.delete_duplicates(node1)
        self.assertEqual(test.next.val, 2)

    def test_delete_duplicates_2(self):
        node5 = ListNode(3, None)
        node4 = ListNode(3, node5)
        node3 = ListNode(2, node4)
        node2 = ListNode(1, node3)
        node1 = ListNode(1, node2)
        test = self.leet83.delete_duplicates(node1)
        self.assertEqual(test.next.next.val, 3)


if __name__ == "__main__":
    unittest.main()
