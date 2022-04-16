# /usr/bin/env python3.6

# https://leetcode.com/problems/implement-strstr/


class Leet28(object):
    def str_str(self, haystack, needle):
        """
        Return the index of the first occurance of needle in haystack.
        If needle is not in haystack, return -1.

        Args:
            haystack -- A string.
            needle -- A string that is potential substring of haystack.

        Returns:
            An integer representing an index or -1.
        """

        # Time: O(n) in total.
        # Space: O(1).
        if needle in haystack:  # O(n)
            return haystack.index(needle)  # O(n)

        return -1

