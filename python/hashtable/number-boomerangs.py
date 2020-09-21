#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
447. Number of Boomerangs

Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k)
such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are
all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/27
"""
from collections import defaultdict


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        for x1, y1 in points:
            dmap = defaultdict(int)
            for x2, y2 in points:
                dmap[(x1-x2)**2 + (y1-y2)**2] += 1
            for d, n in dmap.items():
                ans += n * (n-1)

        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]))
