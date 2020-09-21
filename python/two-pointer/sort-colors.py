#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
75. Sort Colors

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent,
with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's,
then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/11/30
"""
from collections import defaultdict


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()

    def sort_colors_by_dict(self, nums):
        """
        Time: O(n)
        Space: O(n)
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        color_count = defaultdict(int)

        for num in nums:
            color_count[num] += 1

        red = color_count.get(0, 0)
        white = color_count.get(1, 0)
        blue = color_count.get(2, 0)

        nums[:red] = [0] * red
        nums[red:red+white] = [1] * white
        nums[red+white:] = [2] * blue

    def sort_colors(self, nums):
        """
        Time: O(n)
        Space: O(1)
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, front, end = 0, 0, len(nums)-1

        while i <= end:
            if nums[i] < 1:
                nums[front], nums[i] = nums[i], nums[front]
                front += 1
                i += 1
            elif nums[i] > 1:
                nums[end], nums[i] = nums[i], nums[end]
                end -= 1
            else:
                i += 1

if __name__ == "__main__":
    solution = Solution()
    test1 = [0, 2, 1, 2, 1, 0, 0, 2, 1, 2, 1, 1]
    solution.sort_colors(test1)
    print(test1)
