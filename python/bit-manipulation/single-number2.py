#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
137. Single Number II

Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Subscribe to see which companies asked this question

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/20
"""
from collections import defaultdict


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = defaultdict(int)

        for num in nums:
            d[num] += 1

        for k, v in d.items():
            if v == 1:
                return k

    def single_number(self, nums):
        """
        把每一个数对应位相加对3取余, 就是single number对应位的数字
        :param nums: List[int]
        :return: int
        """
        res = 0

        for i in range(32):
            sums = 0
            for num in nums:
                sums += (num >> i) & 1
            res |= (sums % 3) << i

        return res


if __name__ == "__main__":
    solution = Solution()
    test = [1, 1, 1, 2]
    print(solution.singleNumber(test))
    print(solution.single_number(test))
