#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string
Given a string s and a non-empty string p,
find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only
and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/28
"""


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ans = []
        cnt = [0] * 26
        for c in p:
            cnt[ord(c)-ord('a')] += 1

        for i in range(len(s)-len(p)+1):
            tmp = [0] * 26
            for j in range(len(p)):
                tmp[ord(s[i+j])-ord('a')] += 1
            if self.check(cnt, tmp):
                ans.append(i)

        return ans

    def check(self, cnt, tmp):
        for i in range(26):
            if cnt[i] != tmp[i]:
                return False
        return True

if __name__ == "__main__":
    solution = Solution()
