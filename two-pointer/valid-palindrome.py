#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.
For the purpose of this problem, we define empty string as valid palindrome.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/11/25
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = ''.join([c.lower() for c in s if c.isalnum()])

        return res == res[::-1]

    def ispalindrome(self, s):
        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i, j = i+1, j-1

        return True


if __name__ == '__main__':
    solution = Solution()
    test_str1 = "A man, a plan, a canal: Panama"
    test_str2 = "asdfasdfas"
    test_str3 = "0P"
    assert solution.isPalindrome(test_str1)
    assert not solution.isPalindrome(test_str2)
    assert not solution.isPalindrome(test_str3)

    assert solution.ispalindrome(test_str1)
    assert not solution.ispalindrome(test_str2)
    assert not solution.ispalindrome(test_str3)
