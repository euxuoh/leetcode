#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/1/9
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i, e in enumerate(strs[0]):
            for string in strs[1:]:
                if i >= len(string) or e != string[i]:
                    return strs[0][:i]
        return strs[0]


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["aa", "a"]))
