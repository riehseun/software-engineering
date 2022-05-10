# /usr/bin/env python3.6

# https://leetcode.com/problems/substring-with-concatenation-of-all-words/


class Leet30(object):
    def substring_with_concatenation_of_all_words(self, s, words):
        """
        Find the substrings in string where substring can be constrcuted
        by strings given in "words" list.

        Args:
            s -- A string.
            words -- A list of substrings.
        Returns:
            The indexes of substring that can be constructed by
            concatenating strings in words in all possible way.
        """

        return