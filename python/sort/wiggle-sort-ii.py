#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
324. Wiggle Sort II

Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/6
"""


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        mid = (len(nums) - 1) // 2
        nums.sort()
        nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]


if __name__ == "__main__":
    l = [1, 5, 1, 1, 6, 4]
    Solution().wiggleSort(l)
    print(l)
