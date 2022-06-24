# /usr/bin/env python3.6

# https://leetcode.com/problems/regular-expression-matching/


class Leet10(object):
    def is_match(self, s, p):
        """
        Implements regular expression matching.
        * indicates "zero or more" of a preceeding element.
        . indicates any single character.

        Args:
            s -- An input string.
            p -- A pattern.

        Returns:
            True if regular expression matches. False otherwise
        """

        # Example
        # s = "aab"
        # p = "c*a*b"

        # Y if substring in p matches substing in s. N otherwise.
        #       c * a * b
        #     0 1 2 3 4 5
        #   0 Y N Y N Y N
        # a 1 N N N Y Y N
        # a 2 N N N N Y N
        # b 3 N N N N N Y



        return
