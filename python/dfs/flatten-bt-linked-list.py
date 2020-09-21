#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
114. Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/4/3
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        """展开后的树，每一个节点的右孩子都是先序遍历的下一个节点
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        pointer = TreeNode(None)
        stack = [root]

        while stack:
            top = stack.pop()
            if top is None:
                continue
            stack.append(top.right)
            stack.append(top.left)
            pointer.right = top
            pointer.left = None
            pointer = top

    def flatten_recu(self, root):
        """右-左-根
        :param root:
        :return:
        """
        self.pointer = None

        def traverse(node):
            if node is None:
                return
            traverse(node.right)
            traverse(node.left)
            node.right = self.pointer
            node.left = None
            self.pointer = node

        traverse(root)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)

    Solution().flatten_recu(root)

    print(root.val)
    print(root.right.val)
    print(root.right.right.val)
    print(root.right.right.right.val)
    print(root.right.right.right.right.val)
    print(root.right.right.right.right.right.val)
