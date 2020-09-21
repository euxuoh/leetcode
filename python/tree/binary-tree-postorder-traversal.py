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
    def postorderTraversalRecursive(self, root):
        result = []
        self.postorderRecursive(root, result)
        return result

    def postorderRecursive(self, root, res):
        if root:
            self.postorderRecursive(root.left, res)
            self.postorderRecursive(root.right, res)
            res.append(root.val)

    def postorderTraversalIterative(self, root):
        if not root:
            return

        stack, result = [], []
        node = root
        stack.append(node)

        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            result.append(node.val)

        return result[::-1]

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(6)
    root.left.left.right = TreeNode(7)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    print(Solution().postorderTraversalRecursive(root))
    print(Solution().postorderTraversalIterative(root))
