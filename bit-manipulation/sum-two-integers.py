#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
371. Sum of Two Integers

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/8
"""


class Solution(object):
    def getSum(self, a, b):
        """大坑！！！
        python 没有无符号右移，并且当左移操作的结果超过最大整数范围时，会自动将int转为long
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        MASK = 0x100000000

        while b:
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK

        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)


if __name__ == "__main__":
    solution = Solution()
    print(solution.getSum(-12, -8))
