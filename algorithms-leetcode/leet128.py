# /usr/bin/env python3.6

# https://leetcode.com/problems/longest-consecutive-sequence/


class Leet128(object):
    def longest_consecutive(self, nums):
        """
        Finds the length of the longest consecutive sequence.

        Args:
            An array of numbers.

        Returns:
            The length of the longest consecutive sequence.
        """

        # Example: [100,4,200,1,3,2]
        # 100 -> while condition fails
        # 4 -> if condition fails
        # 200 -> while condition fails
        # 1 -> 2 -> 3 -> 4 (max_length = 4)
        # 3 -> if condition fails
        # 2 -> if condition fails
        # Time: O(n) Only checks each element once.

        # Key idea: convert an input array to a set to make search O(1)
        nums = set(nums)
        max_length = 0

        for num in nums:
            if num-1 not in nums:  # This prevents duplicate work
                current_length = 1

                while num+1 in nums:
                    current_length += 1
                    num += 1

                max_length = max(max_length, current_length)

        return max_length
