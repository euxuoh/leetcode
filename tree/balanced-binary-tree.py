#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/2/28
"""


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def height(self, root):
        if root is None:
            return 0

        return max(self.height(root.left), self.height(root.right)) + 1

    def is_balanced(self, root):
        """
        The first method checks whether the tree is balanced strictly according to the definition of
        balanced binary tree: the difference between the heights of the two sub trees are not bigger
        than 1, and both the left sub tree and right sub tree are also balanced. With the helper function depth().

        For the current node root, calling depth() for its left and right children actually
        has to access all of its children, thus the complexity is O(N). We do this for each
        node in the tree, so the overall complexity of isBalanced will be O(N^2). This is a top down approach.
        :param root: TreeNode
        :return: bool
        """
        if root is None:
            return True

        left = self.height(root.left)
        right = self.height(root.right)

        return abs(left - right) <= 1 and self.is_balanced(root.left) and self.is_balanced(root.right)

    def dfs_height(self, root):
        if root is None:
            return 0

        left, right = self.dfs_height(root.left), self.dfs_height(root.right)
        if left < 0 or right < 0 or abs(left - right) > 1:
            return -1

        return max(left, right) + 1

    def is_balanced_dfs(self, root):
        """
        The second method is based on DFS. Instead of calling depth() explicitly for each child node,
        we return the height of the current node in DFS recursion. When the sub tree of the current
        node (inclusive) is balanced, the function dfsHeight() returns a non-negative value as the height.
        Otherwise -1 is returned. According to the leftHeight and rightHeight of the two children, the
        parent node could check if the sub tree is balanced, and decides its return value.

        In this bottom up approach, each node in the tree only need to be accessed once.
        Thus the time complexity is O(N), better than the first solution.
        :param root: TreeNode
        :return: bool
        """
        return self.dfs_height(root) >= 0


if __name__ == "__main__":
    pass
