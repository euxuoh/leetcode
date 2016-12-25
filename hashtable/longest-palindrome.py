#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
409. Longest Palindrome

Given a string which consists of lowercase or uppercase letters,
find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/26
"""
from collections import Counter


class Solution(object):
    def longestPalindrome(self, s):
        """
        统计每个字母的出现次数：
            若字母出现偶数次，则直接累加至最终结果
            若字母出现奇数次，则将其值-1之后累加至最终结果
            若存在出现奇数次的字母，将最终结果+1
        :type s: str
        :rtype: int
        """
        ans = odd = 0
        for k, v in Counter(s).items():
            ans += v
            if v % 2 == 1:
                ans -= 1
                odd += 1

        return ans + (odd > 0)


if __name__ == "__main__":
    pass
