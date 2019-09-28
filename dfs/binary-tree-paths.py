#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
257. Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
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
    def binaryTreePaths(self, root):
        """dfs
        :type root: TreeNode
        :rtype: List[str]
        """
        self.ans = []
        if root is None:
            return self.ans

        def dfs(root, path):
            if root.left is None and root.right is None:
                self.ans += path,
            if root.left:
                dfs(root.left, path + "->" + str(root.left.val))
            if root.right:
                dfs(root.right, path + "->" + str(root.right.val))

        dfs(root, str(root.val))
        return self.ans

    def binary_tree_paths(self, root):
        """pythonic dfs
        :param root:
        :return:
        """
        if root is None:
            return []
        return [str(root.val) + '->' + path
                for kid in (root.left, root.right) if kid
                for path in self.binary_tree_paths(kid)] or [str(root.val)]

    def binary_tree_paths_bfs(self, root):
        """bfs
        :param root:
        :return:
        """
        from collections import deque
        if root is None:
            return []

        queue = deque([[root, str(root.val)]])
        ans = []
        while queue:
            front, path = queue.popleft()
            if front.left is None and front.right is None:
                ans += path,
                continue
            if front.left:
                queue += [front.left, path + '->' + str(front.left.val)],
            if front.right:
                queue += [front.right, path + '->' + str(front.right.val)],
        return ans


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    print(Solution().binaryTreePaths(root))
    print(Solution().binary_tree_paths(root))
    print(Solution().binary_tree_paths_bfs(root))
