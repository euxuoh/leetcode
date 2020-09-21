#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/6
"""
from .listnode import ListNode


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = new_list = ListNode(-1)

        while l1 and l2:
            if l1.val < l2.val:
                p.next, l1 = l1, l1.next
            else:
                p.next, l2 = l2, l2.next
            p = p.next

        p.next = l1 or l2
        return new_list.next


if __name__ == "__main__":
    pass
