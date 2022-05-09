# /usr/bin/env python3.6

# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Leet3(object):
    def length_of_longest_substring(self, s):
        """
        Find the length of the longest substring without repeating
        characters.

        Args:
            s -- Input string.

        Returns:
            Length of longest substring without repeating characters.
        """

        # Stores potential maximum length.
        max_len = 0
        # Two indexes are tracked to compute the length when duplicate
        # character is found.
        start_index = 0
        end_index = 0
        # Hashmap to store character and its index.
        char_and_index_map = {}

        # Time: O(n) iterate through string length n char by char.
        # Space: O(1) dictionary keys are unique and there is finite
        #             number of alphabet characters.
        for i in range(len(s)):
            # If a duplicate char is found.
            if s[i] in char_and_index_map:
                # KEY observation:
                # 1. length must be computed before the start_index is
                # updated.
                # 2. update start_index to begin the next search.
                # 3. Remove all characters whose indexes are less than
                # the start_index.
                max_len = max(max_len, end_index-start_index)
                start_index = char_and_index_map[s[i]] + 1
                # This keeps elements in the dictionary whose value
                # (index) is greater than or equal to start_index.
                # Time: O(1) there is only finite number of alphabet
                # characters.
                char_and_index_map = {k: v for k, v
                    in char_and_index_map.items() if v >= start_index}
                char_and_index_map[s[i]] = i

            # Stores the character and its index in hashmap.
            char_and_index_map[s[i]] = i
            end_index += 1

        # If there is no duplicate character in the stinrg, then should
        # return (end_index-start_index).
        return max(max_len, end_index-start_index)
