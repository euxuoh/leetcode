#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
61. Rotate List

Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/11/30
"""
from listnode import create_list, ListNode


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        # 链表成环, 并计算长度
        length, cur = 1, head
        while cur.next:
            cur = cur.next
            length += 1
        cur.next = head
        cur, tail = head, cur
        for _ in xrange(length - k % length):
            tail = cur
            cur = cur.next
        tail.next = None

        return cur

    def rotate_without_count(self, head, k):
        """不需要计算链表的长度, 但是当K很大时, 会遍历多次, 浪费时间
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        slow, fast = head, head

        for i in range(k):
            if not fast.next:
                fast = head
            else:
                fast = fast.next

        while fast.next:
            slow, fast = slow.next, fast.next

        fast.next = head
        ans = slow.next
        slow.next = None

        return ans


if __name__ == "__main__":
    solution = Solution()
    l = create_list(range(1, 6))
    print(solution.rotateRight(l, 2))
    print(solution.rotate_without_count(create_list(range(1, 6)), 2))
