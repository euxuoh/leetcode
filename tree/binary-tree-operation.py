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


class TreeManipulation(object):
    def search_tree(self, root, val):
        if root is None:
            return None

        if root.val == val:
            return root
        else:
            if not self.search_tree(root.left, val):
                return self.search_tree(root.right, val)
            return root

    def max_depth(self, root):
        if root is None:
            return 0

        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1

    def invert_tree_recursive(self, root):
        if root:
            root.left, root.right = self.invert_tree_recursive(root.right), \
                                    self.invert_tree_recursive(root.left)
            return root

    def invert_tree_interative(self, root):
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right

        return root

    def is_same_tree(self, p, q):
        if p is None and q is None:
            return True

        if p and q and p.val == q.val:
            if self.is_same_tree(p.left, q.left):
                if self.is_same_tree(p.right, q.right):
                    return True

        return False

    def is_balanced(self, root):
        if root is None:
            return True

        left = self.max_depth(root.left)
        right = self.max_depth(root.right)

        return abs(left - right) <= 1 and self.is_balanced(root.left) and self.is_balanced(root.right)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(6)
    root.left.left.right = TreeNode(7)
    root.left.left.right.left = TreeNode(8)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)

    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)

    b = TreeNode(1)
    b.left = TreeNode(2)
    b.right = TreeNode(3)

    # print(TreeManipulation().search_tree(root, 6).val)
    # print(TreeManipulation().max_depth(root))
    print(TreeManipulation().is_same_tree(a, b))
