#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/7
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        1. Integers in each row are sorted from left to right.
        2. The first integer of each row is greater than the last integer of the previous row.
        :param matrix: List[List[int]]
        :param target: int
        :return: bool
        """
        rows = len(matrix)
        if rows == 0:
            return False

        cols = len(matrix[0])
        if cols == 0:
            return False

        left, right = 0, rows * cols - 1

        while left <= right:
            mid = left + (right - left) // 2
            num = matrix[mid // cols][mid % cols]
            if num == target:
                return True
            elif num < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

    def searchMatrix2(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        if rows == 0:
            return False

        cols = len(matrix[0])
        if cols == 0:
            return False

        i, j = 0, cols-1
        while i < rows and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1

        return False


if __name__ == "__main__":
    pass
