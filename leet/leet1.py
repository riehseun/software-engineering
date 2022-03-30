# /usr/bin/env python3.6

# https://leetcode.com/problems/two-sum/


class Leet1(object):
    def two_sum(self, nums, target):
        """
        Find two integers whose indexes correspond to two numbers that
        add up to the target.

        Args:
            nums -- List of integers.
            target - An integer.

        Returns:
            List of two integers whose indexes correspond to two numbers
            that add up to the target.
        """

        num_table = {}

        # Create a hashmap where the number is key and index is value.
        # O(n)
        for i in range(len(nums)):
            if nums[i] not in num_table:
                num_table[nums[i]] = [i]
            else:
                num_table[nums[i]].append(i)

        # Loop though the list and check if (target - num) exists in
        # dictionary. O(n)
        for num in nums:
            # Search by key in a hash table. O(1)
            if target - num in num_table:
                # Two numbers are different, so there is only 1 element
                # in the list, which is the value of dictionary.
                if num != target - num:
                    return [num_table[num][0],num_table[target-num][0]]
                # Two numbers are the same, so there are more than 1
                # element in the list, which is the value of dictionary.
                else:
                    # Make sure two numbers are different elements.
                    if len(num_table[num]) > 1:
                        return [num_table[num][0],num_table[num][1]]

        return []
