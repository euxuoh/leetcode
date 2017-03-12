#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/7
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left, right = 1, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            if mid > x//mid:
                right = mid - 1
            else:
                left = mid + 1

        return left - 1

    def sqrt(self, x):
        left, right = 1, x
        while left <= right:
            mid = left + (right - left) // 2
            if mid >= x // mid:
                right = mid - 1
            else:
                left = mid + 1
        return left == x / left

    def is_perfect_square(self, num):
        x = self.sqrt(num)
        return x == num / x

    def guess_number(self, n, given):
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if mid < given:
                left = mid + 1
            elif mid > given:
                right = mid - 1
            else:
                return mid

    def pow(self, x, n):
        if n == 0:
            return 1

        if n < 0:
            n, x = -n, 1/x

        return self.pow(x*x, n/2) if n % 2 == 0 else x * self.pow(x*x, n//2)

if __name__ == "__main__":
    # print(Solution().mySqrt(16))
    # for i in range(1, 16):
    #     print(i, Solution().sqrt(i))
    # print(Solution().guess_number(10, 6))
    import math
    print(Solution().pow(8.88023, -3), math.pow(8.88023, -3))
