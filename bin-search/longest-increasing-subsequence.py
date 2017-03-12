#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
300. Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest
increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore
the length is 4. Note that there may be more than one LIS
combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/7
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LIS = [nums[0]]

        for i in range(len(nums)):
            if nums[i] > LIS[-1]:
                LIS.append(nums[i])
            else:
                pos = self.binary_search(LIS, nums[i])
                LIS[pos] = nums[i]

        # print(LIS)
        return len(LIS)

    def binary_search(self, nums, target):
        left, right = 0, len(nums)

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

if __name__ == "__main__":
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
