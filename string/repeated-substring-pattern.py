#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
459. Repeated Substring Pattern

Given a non-empty string check if it can be constructed by
taking a substring of it and appending multiple copies of
the substring together. You may assume the given string
consists of lowercase English letters only and its length
will not exceed 10000.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/1/4
"""


class Solution(object):
    def repeatedSubstringPattern(self, str):
        """暴力：若可由子串构建，则子串的首字母肯定从下标0开始，子串的长度是字符串长度的约数
        Time: O(k*n)
        :type str: str
        :rtype: bool
        """
        size = len(str)

        for i in range(1, size//2+1):
            if size % i:
                continue
            if str == str[: i] * (size//i):
                return True

        return False

    def repeated_substring_pattern(self, str):
        size = len(str)
        p = self.get_next(str)[-1]
        return p > 0 and size % (size - p) == 0

    def get_next(self, p):
        size = len(p)
        _next = [0] * size

        for i in range(1, size):
            k = _next[i-1]
            while p[i] != p[k] and k:
                k = _next[k-1]
            if p[i] == p[k]:
                _next[i] = k + 1

        return _next


if __name__ == "__main__":
    solution = Solution()
    assert solution.repeatedSubstringPattern('ababab')
    assert solution.repeated_substring_pattern('ababababab')
