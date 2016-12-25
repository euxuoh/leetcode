#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
205. Isomorphic Strings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/29
"""
from collections import defaultdict


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t:
            return True

        s_d = defaultdict(int)
        t_d = defaultdict(int)

        i = 0
        for c in s:
            if c not in s_d:
                s_d[c] = i
                i += 1

        j = 0
        for c in t:
            if c not in t_d:
                t_d[c] = j
                j += 1

        for k in range(len(s)):
            if s_d[s[k]] != t_d[t[k]]:
                return False

        return True

    def isomorphic(self, s, t):
        s2t, t2s = dict(), dict()

        for i in range(len(s)):
            sc, tc = s2t.get(s[i]), t2s.get(t[i])
            if sc is None and tc is None:
                s2t[s[i]], t2s[t[i]] = t[i], s[i]
            elif sc != t[i] or tc != s[i]:
                return False

        return True


if __name__ == "__main__":
    solution = Solution()
    assert solution.isomorphic('', '')
    assert solution.isomorphic('egg', 'add')
    assert not solution.isomorphic('foo', 'bar')
    assert solution.isomorphic('paper', 'title')
