# /usr/bin/env python3.6

# https://leetcode.com/problems/palindrome-number/

import math


class Leet9(object):
    def is_palindrom(self, x):
        """
        Check if an input integer is palindrom.

        Args:
            x -- An integer.

        Returns:
            True if an input integer is palindrom. False otherwise.
        """

        # Negative number is not palindrom.
        if x < 0:
            return False

        # Single digit number is palindrom.
        if x >= 0 and x < 10:
            return True

        # If the last digit is 0, number cannot be palindrom.
        if x % 10 == 0:
            return False

        # Stores the reversed integer.
        num_reverse = 0

        # Exactly half of the number is reversed when the original is
        # less than the reversed.
        # Time: O(n/2) reverses only the half of input length.
        # Space: O(n/2) stores only the half of input length.
        while x > num_reverse:
            # Get the last digit of the original number.
            last_digit = x % 10
            # Remove the last digit from the original number.
            x = math.trunc(x/10)
            # Construct the reversed integer.
            num_reverse = 10*num_reverse + last_digit

        if num_reverse == x:
            return True
        else:
            # If the original number had an odd number of digits,
            # the middle number would be the last digit of the reversed.
            if math.trunc(num_reverse/10) == x:
                return True

        return False
