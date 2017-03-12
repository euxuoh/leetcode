#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
153. Find Minimum in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/7
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right and nums[left] > nums[right]:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


if __name__ == "__main__":
    print(Solution().findMin([1]))
    print(Solution().findMin([1, 2]))
    print(Solution().findMin([2, 1]))
    print(Solution().findMin([3, 1, 2]))
    print(Solution().findMin([2, 3, 1]))
