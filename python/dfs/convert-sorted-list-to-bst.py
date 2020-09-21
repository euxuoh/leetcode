#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
109. Convert Sorted List to Binary Search Tree

Given a singly linked list where elements are sorted in
ascending order, convert it to a height balanced BST.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/4/4
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    head = None

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        current, length = head, 0
        while current:
            current, length = current.next, length+1
        self.head = head
        return self.recursive(0, length)

    def recursive(self, start, end):
        if start == end:
            return None

        mid = (start+end) // 2
        left = self.recursive(start, mid)
        current = TreeNode(self.head.val)
        current.left = left
        self.head = self.head.next
        current.right = self.recursive(mid+1, end)

        return current


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    result = Solution().sortedListToBST(head)
    print(result.val)
    print(result.left.val)
    print(result.right.val)
