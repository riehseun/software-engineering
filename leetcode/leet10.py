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

        # Example 1
        # s = "aab"
        # p = "c*a*b"

        # Y if substring in p matches substing in s. N otherwise.
        #       c * a * b
        #     0 1 2 3 4 5
        #   0 Y N Y N Y N
        # a 1 N N N Y Y N
        # a 2 N N N N Y N
        # b 3 N N N N N Y

        # Example 2
        # s = "ab"
        # p = ".*"

        # Y if substring in p matches substing in s. N otherwise.
        #       . *
        #     0 1 2
        #   0 Y Y Y
        # a 1 N Y Y
        # b 2 N N Y

        # Example 3
        # s = "a"
        # p = ".*..a*"
        #       . * . . a *
        #     0 1 2 3 4 5 6
        #   0 Y N Y N N N N
        # a 1 N Y Y Y N N N

        # Time: O(len(p)*len(s)) 2D table.
        # Space: O(len(p)*len(s)) 2D table.

        # Initialize 2D array.
        dp = []
        for i in range(0, len(s)+1):
            dp.append([])
            for j in range(0, len(p)+1):
                dp[i].append(" ")

        # An empty pattern always mathes an empty string.
        dp[0][0] = "Y"

        # First row for a pattern to match an empty char in string.
        for j in range(1, len(p)+1):
            # For * to match an empty string, everything up to the last
            # two characters needs to match and the preceeding char
            # can be anything.
            if p[j-1] == "*":
                if dp[0][j-2] == "Y":
                    dp[0][j] = "Y"
                else:
                    dp[0][j] = "N"
            else:
                dp[0][j] = "N"

        # First column for an empty char in pattern to match any char
        # in string.
        for i in range(1, len(s)+1):
            dp[i][0] = "N"

        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                # If two characters match, Then two substrings
                # without these two characters will be the result.
                if s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    if p[j-1] == "*":
                        # In this case, p[j-2] is important.
                        # This mean any character is repeated zero
                        # or more times, so the pattern will match
                        # all possible scenarios.
                        if p[j-2] == s[i-1] or p[j-2] == ".":
                            if (dp[i][j-2] == "Y" \
                                or dp[i-1][j-2] == "Y" \
                                or dp[i-1][j] == "Y"):
                                # One of three conditions satisfied.
                                dp[i][j] = "Y"
                            else:
                                dp[i][j] = "N"
                        else:
                            dp[i][j] = dp[i][j-2]
                    # In this case, pattern can be any character to
                    # satisfy this condition: s[j-1] == p[j-1]
                    elif p[j-1] == ".":
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = "N"

        # Debugging
        # for i in range(0, len(s)+1):
        #     for j in range(0, len(p)+1):
        #         print(dp[i][j])
        #     print("\n")

        if dp[len(s)][len(p)] == "Y":
            return True
        else:
            return False
