# /usr/bin/env python3.6

# https://leetcode.com/problems/set-matrix-zeroes/


class Leet73(object):
    def set_zeroes(self, matrix):
        """
        If an element is 0, set entire row and column to 0.

        Args:
            matrix -- An array of arrays.

        Returns:
            matrix modified in place.
        """

        # Key idea: use a dictionary to store which rows and columns
        #           should be set to 0.
        rows = {}
        cols = {}

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in rows or j in cols:
                    matrix[i][j] = 0
