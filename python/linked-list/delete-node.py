#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
237. Delete Node in a Linked List

Write a function to delete a node (except the tail) in a singly linked list,
given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3,
the linked list should become 1 -> 2 -> 4 after calling your function.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/6
"""
from .listnode import ListNode


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node and node.next:
            delete_node = node.next
            node.val = node.next.val
            node.next = node.next.next
            del delete_node


if __name__ == "__main__":
    pass
