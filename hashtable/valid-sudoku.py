#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
36. Valid Sudoku

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/28
"""


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            row = [board[i][j] for j in range(9)]
            col = [board[j][i] for j in range(9)]
            if not self.isvalid_list(row) or not self.isvalid_list(col):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                clock = [board[i + _i][j + _j] for _i in range(3) for _j in range(3)]
                if not self.isvalid_list(clock):
                    return False

        return True

    def isvalid_list(self, l):
        filter_l = []
        for v in l:
            if v != '.':
                if int(v) < 1 or int(v) > 9:
                    return False
                filter_l.append(v)
        return len(set(filter_l)) == len(filter_l)


if __name__ == "__main__":
    solution = Solution()
    b = [['1', '1', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '2', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '3', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '4', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '5', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '6', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '7', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '8', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', '9']]
    print(solution.isValidSudoku(board=b))
