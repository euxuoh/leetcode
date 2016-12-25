#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
202. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum
of the squares of its digits, and repeat the process until
the number equals 1 (where it will stay), or it loops endlessly
in a cycle which does not include 1. Those numbers for which this
process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/27
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        look_up = {}
        while n != 1 and n not in look_up:
            look_up[n] = True
            n = self.next_number(n)

        return n == 1

    def next_number(self, n):
        sums = 0
        while n:
            digit = n % 10
            sums += digit ** 2
            n //= 10
        return sums

    def next_number2(self, n):
        return sum([int(ch)**2 for ch in str(n)])


if __name__ == "__main__":
    solution = Solution()
    assert solution.isHappy(19)
    # print(solution.next_number(19))
