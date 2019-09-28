#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
117. Populating Next Right Pointers in Each Node II

Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree?
Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/4/3
"""


# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution(object):
    def connect(self, root):
        """
        :param root: a tree link node
        :return: nothing
        """
        head = root
        while head:
            prev, cur, next_head = None, head, None
            while cur:
                if next_head is None:
                    if cur.left:
                        next_head = cur.left
                    elif cur.right:
                        next_head = cur.right

                if cur.left:
                    if prev:
                        prev.next = cur.left
                    prev = cur.left

                if cur.right:
                    if prev:
                        prev.next = cur.right
                    prev = cur.right

                cur = cur.next

            head = next_head

    def connect_level(self, root):
        """层次遍历
        :param root:
        :return:
        """
        if root is None:
            return None

        current = [root]

        while current:
            next_level = []
            size = len(current)
            for i, node in enumerate(current):
                if i < (size - 1):
                    node.next = current[i+1]
                else:
                    node.next = None

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            current = next_level


if __name__ == "__main__":
    # root, root.left, root.right = TreeLinkNode(1), TreeLinkNode(2), TreeLinkNode(3)
    # root.left.left, root.left.right, root.right.right = TreeLinkNode(4), TreeLinkNode(5), TreeLinkNode(7)
    # Solution().connect_level(root)
    # print(root)
    # print(root.left)
    # print(root.left.left)
    Solution().connect_level(None)
