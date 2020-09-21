#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
28. Implement strStr()

Implement strStr().

Returns the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/1/9
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i: i+len(needle)] == needle:
                return i
        return -1

    def str_str(self, haystack, needle):
        _next = self.get_next(needle)
        i, j = 0, 0
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i, j = i+1, j+1
            else:
                j = _next[j]

        if j == len(needle):
            return i - j
        else:
            return -1

    def get_next(self, p):
        _next = [-1]
        k, j = -1, 0

        while j < len(p) - 1:
            if k == -1 or p[k] == p[j]:
                k, j = k + 1, j + 1
                _next.append(k)
            else:
                k = _next[k]

        return _next


if __name__ == "__main__":
    solution = Solution()
    print(solution.str_str('asefasdfasdf', 'asd'))
