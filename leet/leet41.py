# /usr/bin/env python3.6

# https://leetcode.com/problems/first-missing-positive/


class Leet41(object):
    def first_missing_positive(self, nums):
        """
        Find the smallest missing positive integer.

        Args:
            nums -- Unsorted array of intergers.

        Returns:
            The smallest missing positive integer.

        """

        # [1,4,3,3,3] answer=2, n+1=5+1=6
        # At index 0, we have 1
        # We go to index 1%6-1=1-1=0, and update it such that 1+6=7
        # At index 1, we have 4
        # We go to index 4%6-1=4-1=3, and update it such that 3+6=9
        # At index 2, we have 3
        # We go to index 3%6-1=3-1=2, and update it such at 3+6=9
        # At index 3, we have 9
        # We go to index 9%6-1=3-1=2, and update it such at 9+6=15
        # At index 4, we have 3
        # We go to index 3%6-1=3-1=2, and update it such at 15+6=21
        # [7,4,21,9,3]
        # 4 is the first number <= n=5

        # [3,4,-1,1] => [3,4,0,1] answer=2, n+1=4+1=5
        # At index 0, we have 3
        # We go to index 3%5-1=3-1=2, and update it such that 0+5=5
        # At index 1, we have 4
        # We go to index 4%5-1=4-1=3, and update it such that 1+5=6
        # At index 2, we have 5
        # We go to index 5%5-1=0-1=-1, and update it such that 6+5=11
        # At index 3, we have 6 (updated from previous)
        # We go to index 6%5-1=1-1=0, and update it such at 3+5=8
        # [8,4,5,11]
        # 4 is the first number <= n=4

        # [1,2,0] answer=3, n+1=3+1=4
        # At index 0, we have 1
        # We go to index 1%4-1=1-1=0, and update it such that 1+4=5
        # At index 1, we have 2
        # We go to index 2%4-1=2-1=1, and update it such that 2+4=6
        # At index 2, we have 0
        # We skip
        # [5,6,0]
        # 0 is the first number <= n=3

        # [1,2,3] answer=4, n+1=3+1=4
        # At index 0, we have 1
        # We go to index 1%4-1=1-1=0, and update it such that 1+4=5
        # At index 1, we have 2
        # We go to index 2%4-1=2-1=1, and update it such that 2+4=6
        # At index 2, we have 3
        # We go to index 3%4-1=3-1=2, and update it such that 3+4=7
        # [5,6,7]
        # Nothing is less than n=3

        # [7,8,9,11,12] => [0,0,0,0,0] answer=1, n+1=5+1=6
        # 0 is the first number <= n=5

        # 0 or negative numbers or number greater than n+1 cannot
        # be an answer.
        # In other words, answer lies [1, n+1]. We can formulate it as,
        # If all numbers [1,n] are in nums
        #   return n+1
        # Otherwise
        #   return smallest number in [1,n] that is not in nums

        # Time: O(n)
        # Space: O(1)
        n = len(nums)

        # Set numbers outside [1,n] to 0.
        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = 0

        for i in range(n):
            if nums[i] != 0 and nums[i]%(n+1) <= n:
                nums[(nums[i]%(n+1))-1] += (n+1)

        for i in range(n):
            if nums[i] <= n:
                return i + 1

        return n + 1
