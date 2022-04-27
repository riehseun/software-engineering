# /usr/bin/env python3.6

# https://leetcode.com/problems/longest-palindromic-substring/

import math

from leet9 import Leet9


class Leet5(object):
    def longest_palindrome(self, s):
        """
        Find the longest palindrome substring.

        Args:
            s -- Input string

        Returns:
            The longest palindrome substring. (string)
        """

        start_index = 0
        end_index = len(s) - 1
        turn_to_increase_start_index = True

        # Time: O(n)
        # Space:

        # eabcb
        for length in range(len(s)):



        while end_index - start_index >= length:
            if self.is_string_palindrome(s[start_index:end_index+1]):
                return s[start_index:end_index+1]

            if self.is_string_palindrome(s[start_index+1:end_index+1]):
                return s[start_index+1:end_index+1]

            if self.is_string_palindrome(s[start_index:end_index]):
                return s[start_index:end_index]

            start_index += 1
            end_index -= 1

            # if turn_to_increase_start_index:
            #     start_index += 1
            #     turn_to_increase_start_index = False
            # else:
            #     end_index -= 1
            #     turn_to_increase_start_index = True

        return ""


    def is_string_palindrome(self, s):
        """
        Determine if the string in palindrome or not.

        Args:
            s -- Input string

        Return:
            True if s is palindrome. False otherwise.
        """

        # Time: O(n) to do string slicing.
        # Space:
        if s[::-1] == s:
            return True


        return False
