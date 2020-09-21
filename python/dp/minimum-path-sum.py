#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
64. Minimum Path Sum

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/17
"""


class Solution(object):
    def min_path_sum(self, grid):
        """
        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        :param grid: List[List[int]]
        :return: int
        """
        rows = len(grid)
        cols = len(grid[0])

        for i in range(1, rows):
            grid[i][0] += grid[i-1][0]
        for j in range(1, cols):
            grid[0][j] += grid[0][j-1]

        for i in range(1, rows):
            for j in range(1, cols):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[-1][-1]

if __name__ == "__main__":
    print(Solution().min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
