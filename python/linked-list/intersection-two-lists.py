#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
160. Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/4
"""
from .listnode import ListNode


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA: ListNode
        :type headB: ListNode
        :rtype: ListNode
        """
        if not (headA and headB):
            return None

        pa, pb = headA, headB

        while pa and pb:
            if pa is pb:
                return pa

            pa, pb = pa.next, pb.next

            if pa is pb:
                return pa

            if not pa:
                pa = headB

            if not pb:
                pb = headA

        return pa


if __name__ == "__main__":
    solution = Solution()
    c1 = ListNode(5)
    c2 = ListNode(7)
    ha, ha.next, ha.next.next, ha.next.next.next = ListNode(1), ListNode(3), c1, c2
    hb, hb.next, hb.next.next = ListNode(2), c1, c2
    print(solution.getIntersectionNode(ha, hb))
