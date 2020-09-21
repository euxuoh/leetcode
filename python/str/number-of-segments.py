#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
434. Number of Segments in a String

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/1/4
"""


class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = int(len(s) and s[-1] != ' ')
        for i in range(1, len(s)):
            if s[i] == ' ' and s[i-1] != ' ':
                ans += 1
        return ans

    def count_segments(self, s):
        return len(s.strip().split())


if __name__ == "__main__":
    solution = Solution()
    print(solution.countSegments('   hell, kk    e'))
