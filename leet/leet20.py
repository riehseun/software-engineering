# /usr/bin/env python3.6

# https://leetcode.com/problems/valid-parentheses/

class Leet20(object):
    def is_valid(self, s):
        """
        Evaluates if the open/close pattern of brackets of input string
        is valid or not.

        Args:
            s -- An input string.

        Returns:
            True if bracket patterns are valid. False otherwise.
        """

        stack = []

        # Time: O(n) interate through s.
        # Space: O(n) worst case is every char is appended to stack.
        for char in s:
            # If opening parenthesis, push to stack.
            if char == "(" or char == "[" or char == "{":
                stack.append(char)  # O(1).
            else:
                # If stack is not empty.
                if stack:
                    # If closing parenthesis.
                    if char == ")" or char == "]" or char == "}":
                        # Pop if the top element is the corresponding
                        # opening parenthesis.
                        if ((char == ")" and stack[-1] == "(") or
                            (char == "]" and stack[-1] == "[") or
                            (char == "}" and stack[-1] == "{")):
                            # One of three conditions satisfied.
                            stack.pop()  # O(1).
                        # If not, bracket mismatch.
                        else:
                            return False
                # If expression does not start with (,[,{.
                else:
                    return False

        # If stack is empty.
        if not stack:  # O(1).
            return True

        return False
