# /usr/bin/env python3.6

# https://leetcode.com/problems/group-anagrams/


class Leet49(object):
    def group_anagrams(self, strs):
        """
        Find groups of anagrams from a list of strings.

        Args:
            strs -- An array of strings.

        Returns:
            An array of arrays representing groups of anagrams.
        """

        # Key idea: for each string in the input array, store its
        #           "sorted" version as a key of a dictionary.

        anagrams_dict = {}

        for string in strs:
            string_sorted = ''.join(sorted(string))
            if string_sorted in anagrams_dict:
                anagrams_dict[string_sorted].append(string)
            else:
                anagrams_dict[string_sorted] = [string]

        result = []

        for k,v in anagrams_dict.items():
            result.append(v)

        return result