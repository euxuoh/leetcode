#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/2/27
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversalRecurisive(self, root):
        result = []
        self.inorderRecurisive(root, result)
        return result

    def inorderRecurisive(self, root, res):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            self.inorderRecurisive(root.left, res)
            res.append(root.val)
            self.inorderRecurisive(root.right, res)

    def inorderTraversalIterative(self, root):
        stack, res = [], []

        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(6)
    root.left.left.right = TreeNode(7)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    print(Solution().inorderTraversalRecurisive(root))
    print(Solution().inorderTraversalIterative(root))
