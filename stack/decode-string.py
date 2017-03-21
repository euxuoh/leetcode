#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
394. Decode String
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string
inside the square brackets is being repeated exactly k times. Note
that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra
white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain
any digits and that digits are only for those repeat numbers, k.
For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/20
"""


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        nums, curr, strs = [], [], []
        n = 0
        for c in s:
            if c.isdigit():
                n = n * 10 + ord(c) - ord('0')
            elif c == '[':
                nums.append(n)
                n = 0
                strs.append(curr)
                curr = []
            elif c == ']':
                strs[-1].extend(curr * nums.pop())
                curr = strs.pop()
            else:
                curr.append(c)
        return "".join(str[-1]) if strs else "".join(curr)


if __name__ == "__main__":
    print(Solution().decodeString("3[a2[c]]"))
