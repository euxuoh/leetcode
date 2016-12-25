#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
260. Single Number III

Given an array of numbers nums, in which exactly two elements appear only once and
all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant space complexity?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/15
"""
from functools import reduce
import operator


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = reduce(operator.xor, nums)
        low_bit = xor & -xor
        a = b = 0
        for num in nums:
            if num & low_bit:
                a ^= num
            else:
                b ^= num
        return [a, b]

    def single_number_three_lines(self, nums):
        xor = reduce(operator.xor, nums)
        ans = reduce(operator.xor, (x for x in nums if x & xor & -xor))
        return [ans, ans ^ xor]


if __name__ == "__main__":
    solution = Solution()
    print(solution.singleNumber([1, 2, 1, 3, 2, 5, 5, 6]))
    print(solution.single_number_three_lines([1, 2, 1, 3, 2, 5, 5, 6]))
