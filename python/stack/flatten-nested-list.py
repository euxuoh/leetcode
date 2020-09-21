#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
341. Flatten Nested List Iterator

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may
also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],
By calling next repeatedly until hasNext returns false, the order of
elements returned by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],
By calling next repeatedly until hasNext returns false, the order of
elements returned by next should be: [1,4,6].
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/20
"""


class NestedInteger(object):
    """
    This is the interface that allows for creating nested lists.
    You should not implement it, or speculate about its implementation
    """
    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        self.flat_nested_list(nestedList)

    def flat_nested_list(self, nestedList):
        for e in nestedList[::-1]:
            self.stack.append(e)

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            if isinstance(self.stack[-1], int):
                return True
            self.flat_nested_list(self.stack.pop())
        return False


def flat(nestedList, v):
    for e in nestedList:
        if isinstance(e, list):
            flat(e, v)
        else:
            v.append(e)


if __name__ == "__main__":
    # Your NestedIterator object will be instantiated and called as such:
    i, v = NestedIterator([[1, 1], 2, [3, 3]]), []
    while i.hasNext():
        v.append(i.next())
    print(v)
