# /usr/bin/env python3.6

# https://leetcode.com/problems/longest-increasing-subsequence/


class Leet300(object):
    def length_of_lis(self, nums):
        """
        Find the longest increasing subsequence.

        Args:
            nums -- An array of integers.

        Return:
            The maximum length of increasing subsequence.
        """

        # Example 1: 10,9,2,5,3,7,101,18
        # 10 9 2
        # 5 3
        # 7
        # 101 18

        # Example 2: 0,1,0,3,2,3
        # 0 0
        # 1
        # 3 2
        # 3

        # Example 3: 7,7,7,7,7,7,7
        # 7 7 7 7 7 7 7

        piles = []

        for card in nums:
            # If there is no existing pile, create the first pile
            if not piles:
                piles.append(card)
                continue  # Go to next "i" w/o executing below code.

            card_dealed = False  # Track if card "i" has been dealed.
            for i in range(0, len(piles)):
                # If there is a pile where the number should be placed
                # (because the number is less than equal to the last
                # number in the pile)
                if piles[i] >= card:
                    piles[i] = card
                    card_dealed = True
                    break

            if not card_dealed:
                piles.append(card)

        # print(piles)

        return len(piles)





