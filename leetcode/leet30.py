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

        result = []

        # For this problem, all words have the same length.
        word_length = len(words[0])
        substring_length = word_length * len(words)
        words_converted_to_dict = {}
        for word in words:
            if word in words_converted_to_dict:
                words_converted_to_dict[word] += 1
            else:
                words_converted_to_dict[word] = 0

        # Example: "goodgoodbestword"
        #          ["word","good","best","word"]

        # Run sliding window of substring through s.
        # Time: O(kn) where k = n / word_legnth.
        # Space: O(k) where k = n / word_legnth.
        for i in range(len(s)-substring_length+1):
            # print(i)
            # print(s[i:i+substring_length])

            # Check s[i:substring_length] can be constructed by words.
            # If so, append i to result.

            string_splitted_into_words = {}
            string = s[i:i+substring_length]
            j = 0
            while j < len(string):
                word = string[j:j+word_length]
                # Increment the occurance by 1.
                if word in string_splitted_into_words:
                    string_splitted_into_words[word] += 1
                # Initialize the occurance to 0.
                else:
                    string_splitted_into_words[word] = 0
                j += word_length

            if words_converted_to_dict == string_splitted_into_words:
                result.append(i)

        return result
