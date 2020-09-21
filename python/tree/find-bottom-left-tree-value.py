#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
513. Find Bottom Left Tree Value

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
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        node = root
        queue = [node]

        while queue:
            node = queue.pop(0)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        return node.val

    def find_bottom_left_value(self, root):
        """
        pythonic
        :param root: TreeNode
        :return: int
        """
        queue = [root]

        for node in queue:
            queue += filter(None, (node.right, node.left))

        return node.val


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(6)
    root.left.left.right = TreeNode(7)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    print(Solution().findBottomLeftValue(root))
    print(Solution().find_bottom_left_value(root))
