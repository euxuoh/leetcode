#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
12. Integer to Roman

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

Subscribe to see which companies asked this question
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/1/4
"""


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        num_map = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
                   10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
                   100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        order_keys, ans = sorted(num_map.keys(), reverse=True), ''

        while num > 0:
            for k in order_keys:
                while num // k > 0:
                    num -= k
                    ans += num_map[k]

        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.intToRoman(1))
