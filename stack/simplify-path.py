#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
71. Simplify Path

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/20
"""


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for e in path.split('/'):
            if e == '..' and stack:
                stack.pop()
            elif e != '.' and e != '..' and e:
                stack.append(e)
        return '/' + '/'.join(stack)


if __name__ == "__main__":
    print(Solution().simplifyPath("/"))
    print(Solution().simplifyPath("/a/./b/../../c/"))
