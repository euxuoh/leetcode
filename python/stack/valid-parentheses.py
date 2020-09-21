#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid
but "(]" and "([)]" are not.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/20
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, look_up = [], {'(': ')', '[': ']', '{': '}'}
        for parenthes in s:
            if parenthes in look_up:
                stack.append(parenthes)
            elif len(stack) == 0 or look_up.get(stack.pop()) != parenthes:
                return False
        return len(stack) == 0

if __name__ == "__main__":
    pass
