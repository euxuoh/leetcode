#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
290. Word Pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between
a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.

Notes:
You may assume pattern contains only lowercase letters, and str contains
lowercase letters separated by a single space.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/20
"""


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(pattern) != len(words):
            return False

        p2w, w2p = {}, {}
        for p, w in zip(pattern, words):
            if p not in p2w and w not in w2p:
                p2w[p], w2p[w] = w, p
            elif p not in p2w or w not in w2p:
                return False

        return True

    def word_pattern(self, pattern, str):
        """
        pythonic solution
        :param pattern: str
        :param str: str
        :return: bool
        """
        s = pattern
        words = str.split()
        return map(s.find, s) == map(words.index, words)


if __name__ == "__main__":
    solution = Solution()
    p1 = "abba"
    s1 = "dog cat cat dog"
    p2 = "abba"
    s2 = "dog cat cat fish"
    p3 = "aaaa"
    s3 = "dog cat cat dog"
    p4 = "abba"
    s4 = "dog dog dog dog"
    assert solution.wordPattern(p1, s1)
    assert not solution.wordPattern(p2, s2)
    assert not solution.wordPattern(p3, s3)
    assert not solution.wordPattern(p4, s4)

    print(solution.word_pattern(p2, s2))
