#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
222. Count Complete Tree Nodes

Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last,
is completely filled, and all nodes in the last level are as far
left as possible. It can have between 1 and 2h nodes inclusive
at the last level h.

Subscribe to see which companies asked this question.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/7
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left, right = 0, 0
        lt, rt = root, root
        while lt:
            left += 1
            lt = lt.left
        while rt:
            right += 1
            rt = rt.right

        if left == right:
            return pow(2, left) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(Solution().countNodes(root))
