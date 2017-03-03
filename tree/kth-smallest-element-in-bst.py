#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
230. Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/2/28
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            root = node.right


if __name__ == "__main__":
    root = TreeNode(7)
    root.left = TreeNode(5)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(6)
    root.right = TreeNode(8)
    print(Solution().kthSmallest(root, 5))
