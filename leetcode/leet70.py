# /usr/bin/env python3.6

# https://leetcode.com/problems/climbing-stairs/


class Leet70(object):
    def climb_stairs(self, n):
        """
        It takes n steps to reach the top.
        Each time you can clime 1 or 2 steps.
        Compute distinct ways to climb to reach the top.

        Args:
            n -- Number of steps.

        Returns:
            Distinct wayts to climb to reach the top.
        """

        # Dictionary to store the answer for each n.
        memory = {}
        memory[1] = 1
        memory[2] = 2

        # Example: n=1
        # 1+1
        # 1

        # Example: n=2
        # 1+1, 2
        # 2

        # Example: n=3
        # 1+2, 2+1, 1+1+1
        # 3

        # Example: n=4
        # 1+1+2, 1+2+1, 2+1+1, 2+2, 1+1+1+1
        # 5

        # Example: n=5
        # 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1, 1+2+2, 2+1+2, 2+2+1,
        # 1+1+1+1+1
        # 8

        # Take 1 step and compute (n-1)
        # Take 2 steps and compute (n-2)

        # Time: O(2^n) recursive fabonacci.
        # Space: O(n) using memory dictionary.
        return self.subroutine(n, memory)


    def subroutine(self, n, memory):

        if n in memory:
            return memory[n]

        memory[n] = self.subroutine(n-1, memory) + self.subroutine(n-2, memory)
        return memory[n]

