#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
129. Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only,
each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/4/3
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, val):
            val = val * 10 + node.val

            if node.left is None and node.right is None:
                return val

            sums = 0
            if node.left:
                sums += dfs(node.left, val)
            if node.right:
                sums += dfs(node.right, val)

            return sums

        if root is None:
            return 0
        return dfs(root, 0)


if __name__ == "__main__":
    pass
