#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some
pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array
return its index, otherwise return -1.

You may assume no duplicate exists in the array.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/8
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

    def search2(self, nums, target):
        """
        contain duplicate
        :param nums: List[int]
        :param target: int
        :return: bool
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True

            if nums[left] == nums[mid]:
                left += 1
            elif (nums[left] < nums[mid] and nums[left] <= target < nums[mid]) or \
                 (nums[left] > nums[mid] and not nums[mid] < target <= nums[right]):
                right = mid - 1
            else:
                left = mid + 1

        return False

if __name__ == "__main__":
    print(Solution().search2([3, 5, 1, 3], 3))
    print(Solution().search2([1], 1))
    print(Solution().search2([4, 5, 6, 7, 0, 1, 2], 3))
