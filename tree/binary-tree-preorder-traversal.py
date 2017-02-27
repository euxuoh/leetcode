#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/2/27
"""


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversalRecursive(self, root):
        result = []
        self.preorderRecursive(root, result)
        return result

    def preorderRecursive(self, root, res):
        if root:
            res.append(root.val)
            self.preorderRecursive(root.left, res)
            self.preorderRecursive(root.right, res)

    def preorderTraversalIterative(self, root):
        result, stack = [], []
        while True:
            while root:
                result.append(root.val)
                stack.append(root)
                root = root.left
            if not stack:
                return result
            node = stack.pop()
            root = node.right


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(6)
    root.left.left.right = TreeNode(7)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    print(Solution().preorderTraversalRecursive(root))
    print(Solution().preorderTraversalIterative(root))
