# /usr/bin/env python3.6

# https://leetcode.com/problems/add-binary/


class Leet67(object):
    def add_binary(self, a, b):
        """
        Adds two binary numbers.

        Args:
            a -- A binary number.
            b -- A binary number.

        Returns:
            A binary number which is the sum of a and b.
        """

        a = list(a)
        b = list(b)
        carry = 0
        binary_sum = 0
        c = ""

        # Example: [1,1], [1] => 100
        # sum=2, carry=1, c=0
        # sum=1, carry=1, c=00

        # Time: O(s) where s is the combined lenght of a and b.
        # Space: O(1)
        while a or b:
            if a:
                binary_sum += int(a.pop())
            if b:
                binary_sum += int(b.pop())

            if binary_sum == 2:
                if carry == 1:
                    carry = 1
                    c = "1" + c
                else:
                    carry = 1
                    c = "0" + c
            elif binary_sum == 1:
                if carry == 1:
                    carry = 1
                    c = "0" + c
                else:
                    carry = 0
                    c = "1" + c
            else:
                if carry == 1:
                    carry = 0
                    c = "1" + c
                else:
                    carry = 0
                    c = "0" + c

            binary_sum = 0

        if carry == 1:
            c = "1" + c

        return c

