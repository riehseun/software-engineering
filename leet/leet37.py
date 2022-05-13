# /usr/bin/env python3.6

# https://leetcode.com/problems/sudoku-solver/

import math


class Leet37(object):
    def solve_sudoku(self, board):
        """
        Solves sudoku puzzle. (Modifies the input list in-place)

        Args:
            board -- A list of lists where each list is an array of numbers.

        Returns:
            None
        """

        # Time: O(1)
        # Space: O(1)
        # Operations are constant since the board size if fixed.

        coord = self.get_empty_spot(board)

        # No empty spot means, puzzle is solved.
        if coord == (-1, -1):
            return True

        for number in ["1","2","3","4","5","6","7","8","9"]:
            if self.check_row(board, coord[0], number) \
                and self.check_col(board, coord[1], number) \
                and self.check_square(board, coord[0], coord[1], number):
                # All three conditions met.
                board[coord[0]][coord[1]] = number
                if self.solve_sudoku(board):
                    return True

        # If cannot solve the problem using any numbers (1 to 9) in that
        # coordinate, reset the coordicate and return False.
        board[coord[0]][coord[1]] = "."
        return False


    def get_empty_spot(self, board):
        """
        Find an empty spot on a board.

        Args:
            board - A list of lists representing Sudoku board.

        Returns:
            A tuple representing a coordinate.
        """

        for row in board:  ## Iterate through rows.
            for num in row:  ## Iterate through each col in each row.
                if num == ".":
                    return (board.index(row), row.index(num))

        return (-1, -1)


    def check_row(self, board, row_num, num):
        """
        Check if the number can be inserted into the row.

        Args:
            board - A list of lists representing Sudoku board.
            number -- An integer to be inserted into a row.

        Returns:
            True if the number can be inserted. False otherwise.
        """

        if num in board[row_num]:
            return False

        return True


    def check_col(self, board, col_num, num):
        """
        Check if the number can be inserted into the column.

        Args:
            board - A list of lists representing Sudoku board.
            number -- An integer to be inserted into a column.

        Returns:
            True if the number can be inserted. False otherwise.
        """

        for row in board:
            if row[col_num] == num:
                return False

        return True


    def check_square(self, board, row_num, col_num, num):
        """
        Check if the number can be inserted into the square.

        Args:
            board - A list of lists representing Sudoku board.
            number -- An integer to be inserted into a 3x3 sqaure.

        Returns:
            True if the number can be inserted. False otherwise.
        """

        # If row_num = 1, check rows 0-2.
        # If row_num = 3, check rows 3-5.
        # If row_num = 8, check rows 6-8.

        # print(row_num)
        # print(col_num)

        row_num = int(3*(math.floor(row_num/3)))
        col_num = int(3*(math.floor(col_num/3)))
        # print(row_num)
        # print(col_num)

        for i in range(row_num, row_num+3):
            for j in range(col_num, col_num+3):
                if board[i][j] == num:
                    return False

        return True
