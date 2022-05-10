# /usr/bin/env python3.6

# https://leetcode.com/problems/longest-valid-parentheses/


class Leet32(object):
    def longest_valid_parentheses(self, s):
        """
        Find the longest valid parenthesis.

        Args:
            s -- String representing a parenthesis pattern.
        Returns:
            The longest valid parenthesis.
        """

        # Example: (()
        # stack: ["("]
        # stack: ["(", "("]
        # stack: ["("]

        # Example: ()(()
        # stack: ["("]
        # stack: []
        # stack: ["("]
        # stack: ["(", "("]
        # stack: ["("]

        stack = []
        indexes = {}
        longest = [0]

        # Time: O(n)
        # Space: O(n)
        for i in range(len(s)):
            if s[i] == "(":
                stack.append((i, s[i]))
            else:
                # Found a matching pair
                if len(stack) > 0 and stack[-1][1] == "(":
                    # Keep track of indexes of opening and closing
                    # parenthesis that constitute a valid pattern.
                    indexes[stack[-1][0]] = i
                    stack.pop()
                else:
                    stack.append((i, s[i]))

        # stack will now only contain unmatching parenthesis and thier
        # indices.
        if not stack:
            return len(s)

        a = len(s)
        b = 0
        longest = 0
        while stack:
            b = stack[-1][0]
            longest = max(longest, a-b-1)
            a = b
            stack.pop()

        return max(longest, a)











