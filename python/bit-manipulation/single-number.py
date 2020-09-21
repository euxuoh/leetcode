#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
136. Single Number

Given an array of integers, every element appears twice except for one.
Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/8
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0

        for num in nums:
            res ^= num

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.singleNumber([1, 2, 2, 3, 3, 4, 4]))
