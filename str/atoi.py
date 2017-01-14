#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
8. String to Integer (atoi)

Implement atoi to convert a string to an integer.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/1/12
"""


class Solution(object):
    def atoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        if not str:
            return 0

        i = 0
        while i < len(str) and str[i] == ' ':
            i += 1

        sign = 1
        if str[i] == '+':
            i += 1
        elif str[i] == '-':
            sign = -1
            i += 1

        result = 0
        while i < len(str) and '0' <= str[i] <= '9':
            if result > (MAX_INT - int(str[i]))//10:
                return MAX_INT if sign > 0 else MIN_INT
            result = result * 10 + int(str[i])
            i += 1

        return sign * result


if __name__ == "__main__":
    solution = Solution()
    print(solution.atoi('2147483648'))
