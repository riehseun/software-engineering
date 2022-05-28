import unittest

from leet2 import Leet2, ListNode


class TestLeet2(unittest.TestCase):
    def setUp(self):
        self.leet2 = Leet2()

    def test_add_two_numbers_1(self):
        node9 = ListNode(8, None)
        node8 = ListNode(0, node9)
        node7 = ListNode(7, node8)
        node6 = ListNode(4, None)
        node5 = ListNode(6, node6)
        node4 = ListNode(5, node5)
        node3 = ListNode(3, None)
        node2 = ListNode(4, node3)
        node1 = ListNode(2, node2)
        test = self.leet2.add_two_numbers(node1, node4)
        self.assertEqual(test, node7)


if __name__ == "__main__":
    unittest.main()
