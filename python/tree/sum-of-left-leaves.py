#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

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
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = 0
        queue = [root]

        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
                if not node.left.left and not node.left.right:
                    result += node.left.val
            if node.right:
                queue.append(node.right)

        return result

    def sum_of_left_leaves_recursive(self, root):
        if root is None:
            return 0

        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sum_of_left_leaves_recursive(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(6)
    root.left.left.right = TreeNode(7)
    root.left.left.right.left = TreeNode(8)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)

    print(Solution().sumOfLeftLeaves(root))
    print(Solution().sum_of_left_leaves_recursive(root))
