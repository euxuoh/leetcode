#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
34. Search for a Range

Given an array of integers sorted in ascending order, find the
starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/8
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        import bisect

        left = bisect.bisect_left(nums, target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]

        right = bisect.bisect_right(nums, target)
        return [left, right-1]


if __name__ == "__main__":
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6))
