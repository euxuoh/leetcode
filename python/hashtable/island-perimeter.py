#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
463. Island Perimeter

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/20
"""


class Solution(object):
    def island_perimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0]) if row else 0
        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    if i == 0 or grid[i-1][j] == 0:
                        ans += 1
                    if i == row-1 or grid[i+1][j] == 0:
                        ans += 1
                    if j == 0 or grid[i][j-1] == 0:
                        ans += 1
                    if j == col-1 or grid[i][j+1] == 0:
                        ans += 1
        return ans

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0]) if row else 0
        ans = 0
        for x in range(row):
            for y in range(col):
                if grid[x][y] == 1:
                    ans += 4
                    if x > 0 and grid[x - 1][y]:
                        ans -= 2
                    if y > 0 and grid[x][y - 1]:
                        ans -= 2
        return ans


if __name__ == "__main__":
    solution = Solution()
    g = [[0, 1, 0, 0],
         [1, 1, 1, 0],
         [0, 1, 0, 0],
         [1, 1, 0, 0]]
    print(solution.islandPerimeter(g))
    print(solution.island_perimeter(g))
