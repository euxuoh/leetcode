#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
383. Ransom Note

Given an arbitrary ransom note string and another string containing
letters from all the magazines, write a function that will return
true if the ransom note can be constructed from the magazines;
otherwise, it will return false.

Each letter in the magazine string can only be used once in your
ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/1/4
"""
from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        m_cnt = Counter(magazine)

        for c in ransomNote:
            if c not in m_cnt:
                return False
            m_cnt[c] -= 1
            if m_cnt[c] < 0:
                return False

        return True

    def canconstruct(self, ransom_note, magazine):
        return not Counter(ransom_note) - Counter(magazine)


if __name__ == "__main__":
    solution = Solution()
    assert not solution.canConstruct('a', 'b')
    assert not solution.canConstruct('aa', 'ab')
    assert solution.canConstruct('aa', 'aab')
