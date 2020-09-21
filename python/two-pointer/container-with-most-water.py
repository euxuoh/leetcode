#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container,
such that the container contains the most water.

Note: You may not slant the container.

Tags: array, two pointer, greedy

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@source: https://leetcode.com/problems/container-with-most-water/
@author: houxue
@date: 2016/11/25
"""


class Solution(object):
    def maxArea(self, height):
        """
        设置两个指针i, j, 一头一尾, 相向而行. 假设i指向的挡板较低, j指向的挡板较高(height[i] < height[j]).
        下一步移动哪个指针?
            -- 若移动j, 无论height[j-1]是何种高度, 形成的面积都小于之前的面积.
            -- 若移动i, 若height[i+1] <= height[i], 面积一定缩小; 但若height[i+1] > height[i], 面积则有可能增大.
        综上, 应该移动指向较低挡板的那个指针.

        :type height: List[int]
        :rtype: int
        """
        max_area, i, j = 0, 0, len(height) - 1
        while i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                k = i + 1
                while k < j and height[k] <= height[i]:
                    k += 1
                i = k
            else:
                k = j - 1
                while k > i and height[k] <= height[j]:
                    k -= 1
                j = k
        return max_area


if __name__ == '__main__':
    solution = Solution()
    h = [2, 4, 3, 1, 4]
    result = solution.maxArea(h)
    assert result == 12
