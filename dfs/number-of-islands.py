#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
200. Number of Islands

给定一个由字符‘1’（陆地）和‘0’（水域）组成的二维网格地图，计算岛屿的个数。
岛屿被水域环绕，由竖直或者水平方向邻接的陆地构成。你可以假设网格地图的四条
边都被水域包围。

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/4/4
"""


class Solution(object):
    def numIslands(self, grid):
        """dfs
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        isvisited = [[False for _ in range(cols)] for _ in range(rows)]

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not isvisited[i][j]:
                    self.dfs(grid, isvisited, rows, cols, i, j)
                    count += 1

        return count

    def dfs(self, grid, isvisited, rows, cols, i, j):
        if grid[i][j] == '0' or isvisited[i][j]:
            return
        isvisited[i][j] = True

        if i != 0:
            self.dfs(grid, isvisited, rows, cols, i-1, j)
        if i != rows-1:
            self.dfs(grid, isvisited, rows, cols, i+1, j)
        if j != 0:
            self.dfs(grid, isvisited, rows, cols, i, j-1)
        if j != cols-1:
            self.dfs(grid, isvisited, rows, cols, i, j+1)


if __name__ == "__main__":
    g1 = [list(x) for x in ['11110', '11010', '11000', '00000']]
    g2 = [list(x) for x in ['11000', '11000', '00100', '00011']]
    print(Solution().numIslands(g1))
    print(Solution().numIslands(g2))
    print(Solution().numIslands([]))
