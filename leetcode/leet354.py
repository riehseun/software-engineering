# /usr/bin/env python3.6

# https://leetcode.com/problems/russian-doll-envelopes/

from leet300 import Leet300


class Leet354(object):
    def max_envelopes(self, envelopes):
        """
        Find the maximum possible sum of nodes' value in any path in a
        tree.

        Args:
            envelops -- list of lists that have 2 elements representing
                        width and height.

        Returns:
            The maximum number of putting one envelop over another.
            (the width and height must be greater)
        """

        # Questions:
        # Width and lenght are always greater than 0? Yes.

        # Key idea: sort the envelops according to increasing width but
        #           when the width are the same, sort by height in
        #           reverse order.
        #           Example: [[1,100],[51,70],[51,51],[60,60],[70,70]]
        #           Then, Find the longest increasing subsequence based
        #           on height values.

        heights = []
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        for envelop in envelopes:
            heights.append(envelop[1])

        # print(heights)

        leet300 = Leet300()
        return leet300.length_of_lis(heights)
