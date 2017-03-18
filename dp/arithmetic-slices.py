#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
413. Arithmetic Slices

A sequence of number is called arithmetic if it consists of at least three
elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9

The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array
is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular,
this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/15
"""


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        dp[i]表示到A[i]为止, 等差数列的个数
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        if length < 3:
            return 0
        dp = [0] * length
        if A[0] + A[2] == 2 * A[1]:
            dp[2] = 1
        result = dp[2]

        for i in range(3, length):
            if A[i-2] + A[i] == 2 * A[i-1]:
                dp[i] = dp[i-1] + 1
            result += dp[i]

        return result

if __name__ == "__main__":
    print(Solution().numberOfArithmeticSlices([1, 2, 3, 4]))
