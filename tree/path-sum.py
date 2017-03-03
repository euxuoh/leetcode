#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/1
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        if not root.left and not root.right and root.val == sum:
            return True

        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

    def pathSum(self, root, sum):
        if root is None:
            return []

        if not root.left and not root.right:
            if root.val == sum:
                return [[root.val]]
            else:
                return []

        a = self.pathSum(root.left, sum-root.val) + self.pathSum(root.right, sum-root.val)

        return [[root.val] + i for i in a]


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    print(Solution().pathSum(root, 22))
    sorted([2, 4, 5, 2, 6, 7, 4])
