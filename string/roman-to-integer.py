#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
13. Roman to Integer

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Subscribe to see which companies asked this question

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/1/4
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0

        for i in range(len(s)):
            if i > 0 and num_map[s[i]] > num_map[s[i-1]]:
                ans += num_map[s[i]] - 2 * num_map[s[i-1]]
            else:
                ans += num_map[s[i]]

        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt('MMMCMXCIX'))
