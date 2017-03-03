#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
173. Binary Search Tree Iterator

Implement an iterator over a binary search tree (BST). Your iterator will be
initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory,
where h is the height of the tree.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/1
"""


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.push(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        self.push(node.right)
        return node.val

    def push(self, node):
        """
        :param root:
        :return:
        """
        while node is not None:
            self.stack.append(node)
            node = node.left


if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.left.left = TreeNode(0)
    root.left.right = TreeNode(3)
    root.right = TreeNode(7)
    root.right.left = TreeNode(5)
    root.right.left.left = TreeNode(6)
    root.right.right = TreeNode(8)

    # Your BSTIterator will be called like this:
    i, v = BSTIterator(root), []
    while i.hasNext():
        v.append(i.next())

    print(v)
