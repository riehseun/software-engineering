# /usr/bin/env python3.6

# https://leetcode.com/problems/russian-doll-envelopes/


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

        print(heights)

        # https://segmentfault.com/a/1190000003819886

        # Example: [2,3,5,4,5,6,5,7,8]
        # len = 1 [2] [3] [5] [4] [5] [6] [5] [7] [8]
        # len = 2 [2,3] [3,5] [4,5] [5,6] [5,7] [7,8]
        # len = 3 [2,3,5] [4,5,6] [5,7,8]
        # len = 4
        # len = 5
        # len = 6
        # len = 7

        # tails=[0,0,0,0,0,0,0,0,0] i=0 j=0 m=0 size=1
        # tails[0]=0 < 2
        # tails=[0,2,0,0,0,0,0,0,0] i=1 j=2 m=1 size=2
        # tails[1]=2 < 3
        # tails=[0,2,3,0,0,0,0,0,0] i=2 j=3 m=2 size=3
        # tails[2]=3 < 5
        # tails=[0,2,3,5,0,0,0,0,0] i=3 j=4 m=3 size=4
        # tails[3]=5 > 4
        # tails=[0,2,3,4,0,0,0,0,0] i=3 j=3 size=4
        # ...

        # tails = [0] * len(nums)
        # size = 0
        # for x in nums:
        #     i, j = 0, size
        #     while i != j:
        #         m = (i + j) / 2
        #         if tails[m] < x:
        #             i = m + 1
        #         else:
        #             j = m
        #     tails[i] = x
        #     size = max(i + 1, size)
        # return size



