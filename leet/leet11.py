# /usr/bin/env python3.6

# https://leetcode.com/problems/container-with-most-water/


class Leet11(object):
    def max_area(self, height):
        """

        Args:
            height -- A list of integers.

        Returns:
            The maximum rectangular area that can be covered by two
            heights.
        """

        max_area = 0
        start = 0
        end = len(height) - 1

        # Time: O(n) iterate through array.
        # Space: O(1)
        while start < end:
            width = end - start
            length = min(height[start], height[end])
            area = width * length
            max_area = max(max_area, area)

            # Max area can only be constructed by keeping higher height.
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1

        return max_area