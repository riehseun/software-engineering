# /usr/bin/env python3.6

# https://leetcode.com/problems/reverse-integer/


class Leet7(object):
    def reverse(self, x):
        """

        Args:
            x -- An integer.

        Returns:
            Integer with its digits reversed.
        """

        # Example: 321
        integer = str(x)
        is_negative = False

        if integer[0] == "-":
            is_negative = True
            integer = integer[1:]
            start = 0
            end = len(integer) - 1

        start = 0
        end = len(integer) - 1

        # 123143434
        #   s   e

        # Time: O(n/2)
        # Space: O(n/2) String is immutable, so creates a new one each
        #               time
        while start < end:
            integer = integer[:start] \
                + integer[end] \
                + integer[start+1:end] \
                + integer[start] \
                + integer[end+1:]
            start += 1
            end += -1

        if is_negative:
            if -int(integer) > -(2**31)-1:
                return -int(integer)
            else:
                return 0
        else:
            if int(integer) < 2**31:
                return int(integer)
            else:
                return 0


