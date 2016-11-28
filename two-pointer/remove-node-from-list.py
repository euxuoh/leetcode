#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
19. Remove Nth Node From End of List
Given a linked list, remove the nth node from the end of list and return its head.

For example,
   Given linked list: 1->2->3->4->5, and n = 2.
   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/11/25
"""


def create_list(value):
    head = ListNode(value[0])
    head.next = None
    p = head
    for val in value[1:]:
        node = ListNode(val)
        p.next = node
        p = node

    return head


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self is None:
            return 'Nil'
        else:
            return "{}->{}".format(self.val, repr(self.next))


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        res = ListNode(-1)
        res.next = head
        slow, fast = res, res

        for i in range(n):
            fast = fast.next

        while fast.next:
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next

        return res.next


if __name__ == '__main__':
    solution = Solution()
    l = create_list(range(10))
    print solution.removeNthFromEnd(l, 101)
