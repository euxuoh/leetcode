#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
461. Hamming Distance


The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/20
"""


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        cnt = 0

        while xor:
            cnt += 1
            xor &= xor - 1

        return cnt


if __name__ == "__main__":
    solution = Solution()
    print(solution.hammingDistance(1, 4))
