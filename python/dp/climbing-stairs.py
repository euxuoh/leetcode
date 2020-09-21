#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
70. Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/15
"""


class Solution(object):
    def climb_stairs(self, n):
        """
        上到第n层台阶的方法有两种，分别是从n-1层和n-2层上，所以，
            f(n) = f(n-1) + f(n-2)
        类似斐波那契问题
        :param n: int
        :return: int
        """
        if n <= 0:
            return 0

        a, b = 1, 1
        for _ in range(n):
            a, b = b, a+b
        return a

if __name__ == "__main__":
    print(Solution().climb_stairs(0))
