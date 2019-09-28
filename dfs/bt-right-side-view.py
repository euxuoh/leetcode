#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
199. Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/4/2
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """dfs
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.right_side_view_dfs(root, 1, result)
        return result

    def right_side_view_dfs(self, node, depth, result):
        if node is None:
            return

        if depth > len(result):
            result.append(node.val)

        self.right_side_view_dfs(node.right, depth+1, result)
        self.right_side_view_dfs(node.left, depth+1, result)

    def right_side_view_bfs(self, root):
        if root is None:
            return []

        result, current = [], [root]
        while current:
            size = len(current)
            for i in range(size):
                node = current.pop(0)
                if i == 0:
                    result.append(node.val)
                if node.right:
                    current.append(node.right)
                if node.left:
                    current.append(node.left)
        return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    print(Solution().rightSideView(root))
    print(Solution().right_side_view_bfs(root))
