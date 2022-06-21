# /usr/bin/env python3.6

# https://leetcode.com/problems/3sum/


class Leet15(object):
    def three_sum(self, nums):
        """
        Find unique sets of three intergers that sum to 0.

        Args:
            nums -- A list of integers.

        Returns:
            All unique triplets that sum to zero.
        """

        triplets = []

        if len(nums) < 3:
            return triplets

        # Example: [-1,0,1,2,-1,-4]
        # Sorted: [-4,-1,-1,0,1,2]
        #           s     i     e

        # Example: [0,0,0]
        # Sorted: [0,0,0]
        #          s   e

        nums.sort()  # O(nlogn)

        # Time: O(n^2)
        # Space: O(n) worst case, can append all possible combo into triplets.
        for i in range(len(nums)):
            start = 0
            end = len(nums) - 1
            while start < i and i < end:
                # If the sum is less than zero, need to increment the
                # start index to increase the sum.
                if nums[i] + nums[start] + nums[end] < 0:
                    start += 1
                # If the sum is greater than zero, need to decrement the
                # end index to decrease the sum.
                elif nums[i] + nums[start] + nums[end] > 0:
                    end -= 1
                else:
                    triplets.append([nums[i],nums[start],nums[end]])

                    # We can increment either start or end.
                    if nums[start] <= nums[end]:
                        start += 1
                    else:
                        end -= 1

        # Time: O(n)
        # Space: O(n)
        unique_triplets = []
        for triplet in triplets:
            if triplet not in unique_triplets:
                unique_triplets.append(triplet)

        return unique_triplets