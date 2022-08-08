# /usr/bin/env python3.6

# https://leetcode.com/problems/generate-parentheses/


class Leet22(object):
    def generate_parenthesis(self, n):
        """
        Generate all combinations of well-formed parentheses.

        Args:
            n -- An integer.

        Returns:
            All combinations of well-formed parentheses.
        """

        # Example:
        # n=1 ()
        # n=2 (()) ()()
        # n=3 ((())) (()()) (())() ()(()) ()()()

        # Time: O(2^n) At every index, there are two choices "(" or ")"
        # Space: O(n!)

        combinations = []

        self.subroutine(n, 0, 0, "", combinations)

        return combinations


    def subroutine(self, n, num_open, num_close, string, combinations):
        """
        Generate all combinations of well-formed parentheses.

        Args:
            n -- An integer.
            num_open -- The number of opening brackets used.
            num_close -- The number of closing brackets used.
            string -- Valid parenthesis pattern in construction.
            combinations -- A list of store all valid parenthesis.

        Returns:
            All combinations of well-formed parentheses.
        """

        if num_open == n and num_close == n:
            combinations.append(string)

        if num_open < n:
            # No "return" statement.
            self.subroutine(n, num_open+1, num_close, string+"(", combinations)

        # Number of closing parenthesie cannot exceed the number of
        # opening parenthesis at any point to construct valid patterns.
        if num_close < num_open:
            # No "return" statement.
            self.subroutine(n, num_open, num_close+1, string+")", combinations)


