#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
345. Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/11/26
"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aeiou'
        l = list(s)
        i, j = 0, len(s)-1

        while i < j:
            if l[i].lower() not in vowels:
                i += 1
            elif l[j].lower() not in vowels:
                j -= 1
            else:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1

        return ''.join(l)


if __name__ == "__main__":
    solution = Solution()
    assert solution.reverseVowels('hello') == 'holle'
    assert solution.reverseVowels('leetcode') == 'leotcede'
    assert solution.reverseVowels('aA') == 'Aa'
