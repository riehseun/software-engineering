# /usr/bin/env python3.6

# https://leetcode.com/problems/longest-common-prefix/


class Leet14(object):
    def longest_common_prefix(self, strs):
        """
        Find the longest common prefix string amongst an array of
        strings.

        Args:
            strs -- An array of strings.

        Returns:
            Longest common prefix string.
        """

        common_prefix = ""
        char = None

        # Time: O(s) where s is the combined length of all strings.
        # Space: O(s) worst case is exactly identical strings.
        # Start with the first char in the first string.
        for j in range(len(strs[0])):
            # Assume the first common char will exist in all strings.
            common_char = True
            # Loop through each string and check.
            for i in range(len(strs)):
                # If the index is greater or equal to length of string,
                # then surely the string is shorter and there cannot be
                # common char.
                if j >= len(strs[i]):
                    common_char = False
                    break  # Exit inner loop, no need to proceed.
                if not char:
                    # Assign jth char of ith string to "char" variable.
                    char = strs[i][j]
                if strs[i][j] != char:
                    common_char = False
                    break  # Exit inner loop, no need to proceed.
            if common_char:
                common_prefix += char
                # Reset before starting to scan for the next char.
                char = None
            else:
                break  # Exit outer loop, no need to proceed.

        return common_prefix
