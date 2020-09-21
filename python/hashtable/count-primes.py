#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
204. Count Primes

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/29
"""


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0], is_prime[1] = False, False

        for i in range(2, n):
            if i * i >= n:
                break

            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False

        return sum(is_prime)


if __name__ == "__main__":
    solution = Solution()
    print(solution.countPrimes(25))
