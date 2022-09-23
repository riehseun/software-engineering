# /usr/bin/env python3.6

# https://leetcode.com/problems/length-of-last-word/


class Leet58(object):
    def length_of_last_word(self, s):
        """
        Find the length of last word from input string where each word
        is separated by a space.

        Args:
            s -- Input string.

        Returns:
            Integer representing the length of last word.
        """

        # Time: O(n)
        # Space: O(n)
        # Worst case for both time and space is that every char is
        # separated by a space.
        word_array = s.strip().split(" ")

        return len(word_array[len(word_array)-1])
