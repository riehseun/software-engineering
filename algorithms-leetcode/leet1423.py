# /usr/bin/env python3.6

# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/


class Leet1423(object):
    def max_score(self, card_points, k):
        """
        Number can be taken either from left or right of an input array.
        Find the maximum sum of numbers taken from the input array.

        Args:
            card_points -- An array of numbers.
            k -- The number of times the numbers can be taken out.

        Returns:
            The maximum sum of numbers taken from the input array.
        """

        # Key idea: find the smallest sub-array whose length is
        #           len(card_points)-k

        # Example 1: [1,2,3,4,5,6,1], k=3
        # [1,2,3,4]

        current_sum = sum(card_points[0:len(card_points)-k])
        smallest_sum = current_sum

        # Time: O(n-k) where n is length of card_points
        # Space: O(1)
        for i in range(0, k):
            current_sum = (current_sum
                - card_points[i]
                + card_points[len(card_points)-k+i])
            smallest_sum = min(smallest_sum, current_sum)

        return sum(card_points) - smallest_sum