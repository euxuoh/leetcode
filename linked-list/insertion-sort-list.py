#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
147. Insertion Sort List

Sort a linked list using insertion sort.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/7
"""
from listnode import create_list


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return '{}->{}'.format(self.val, repr(self.next))


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        sorted_tail, cur = head, head.next

        while cur:
            prev = dummy
            while prev.next.val < cur.val:
                prev = prev.next
            if prev == sorted_tail:
                cur, sorted_tail = cur.next, cur
            else:
                cur.next, prev.next, sorted_tail = prev.next, cur, cur.next
                cur = sorted_tail.next

        return dummy.next

    def insert_sort(self, head):
        if head is None:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        q = head.next
        head.next = None

        while q:
            p, cur = dummy, q
            while p.next and p.next.val <= cur.val:
                p = p.next
            q = q.next
            cur.next = p.next
            p.next = cur

        return dummy.next


if __name__ == "__main__":
    solution = Solution()
    l = create_list([3, 2, 4])
    print(solution.insert_sort(l))
