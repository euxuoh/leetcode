#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
344. Reverse String

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/11/25
"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = list(s)
        i, j = 0, len(s) - 1

        while i < j:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1

        return ''.join(string)

    def reverse_string_recursion(self, s):
        l = len(s)
        if l < 2:
            return s
        return self.reverse_string_recursion(s[l/2:]) + self.reverse_string_recursion(s[:l/2])

    def reverse_string_pythonic(self, s):
        return s[::-1]


if __name__ == '__main__':
    solution = Solution()
    test_str = 'hello'
    assert solution.reverseString(test_str) == 'olleh'
    assert solution.reverse_string_recursion(test_str) == 'olleh'
    assert solution.reverse_string_pythonic(test_str) == 'olleh'
