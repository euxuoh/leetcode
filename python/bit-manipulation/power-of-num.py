#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
342. Power of Four

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?

Credits:
Special thanks to @yukuairoy for adding this problem and creating all test cases.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/12
"""


class Solution(object):
    def isPowerOfTwo(self, num):
        """2的幂次方的最高位为1，其余位全为0，所以 n & n-1 == 0
        :type num: int
        :rtype: bool
        """
        # return num > 0 and (num & (num-1)) == 0
        return num > 0 and (num & ~-num) == 0

    def isPowerOfThree(self, num):
        """
        :type num: int
        :rtype: bool
        """
        pass

    def isPowerOfFour(self, num):
        """4的幂次方数的特点：
            1. 最高位为1，其余位全为0, 用isPowerOfTwo()判断
            2. 0的个数为偶数，用(num & 0x55555555 == num)判断
        :type num: int
        :rtype: bool
        """
        return num > 0 and (num & ~-num) == 0 and (num & 0x55555555 == num)

if __name__ == "__main__":
    solution = Solution()
    assert not solution.isPowerOfTwo(0)
    assert solution.isPowerOfTwo(1)
    assert solution.isPowerOfTwo(2)
    assert not solution.isPowerOfTwo(3)

    assert not solution.isPowerOfFour(0)
    assert solution.isPowerOfFour(1)
    assert solution.isPowerOfFour(4)
    assert not solution.isPowerOfFour(15)
