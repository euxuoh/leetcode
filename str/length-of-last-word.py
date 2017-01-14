#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
58. Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/1/9
"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split()[-1]) if len(s.strip().split()) > 0 else 0

    def length_of_last_word(self, s):
        if not s:
            return 0

        cnt = 0
        for c in reversed(s):
            if c == ' ':
                if cnt:
                    break
            else:
                cnt += 1

        return cnt

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLastWord('hello world   '))
    print(solution.length_of_last_word('hello world     '))
