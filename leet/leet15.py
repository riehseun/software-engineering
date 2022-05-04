# /usr/bin/env python3.6

# https://leetcode.com/problems/3sum/


class Leet15(object):
    def three_sum(self, nums):
        """

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

        nums.sort()

        for i in range(len(nums)):
            start = 0
            end = len(nums) - 1
            while end > start:
                if (i != start
                    and i != end
                    and nums[i] + nums[start] + nums[end] == 0):
                    # All 3 conditions satisfied.

                    new = True
                    for triplet in triplets:
                        # Triplet does not already exist.
                        if (nums[i] in triplet
                            and nums[start] in triplet
                            and nums[end] in triplet):
                            new = False
                    if new:
                        triplets.append([nums[i],nums[start],nums[end]])

                # If the sum is less than zero, need to increment the
                # start index to increase the sum.
                if nums[i] + nums[start] + nums[end] < 0:
                    start += 1
                # If the sum is greater than zero, need to decrement the
                # end index to decrease the sum.
                else:
                    end -= 1

            # start = 0
            # end = len(nums) - 1

        return triplets