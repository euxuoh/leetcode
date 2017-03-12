#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
148. Sort List

Sort a linked list in O(n log n) time using constant space complexity.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/6
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        prev, slow, fast = None, head, head

        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        prev.next = None

        sorted_left = self.sortList(head)
        sorted_right = self.sortList(slow)

        return self.merge_list(sorted_left, sorted_right)

    def merge_list(self, l1, l2):
        cur = dummy = ListNode(-1)

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 or l2
        return dummy.next


if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(4)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(1)
    print(Solution().sortList(head))
    sorted()
