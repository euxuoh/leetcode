#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
83. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/4
"""
from listnode import ListNode, create_list


class Solution(object):
    def deleteDuplicates(self, head):
        """
            cur = head
            while cur:
                runner = cur.next
                while runner and runner.val == cur.val:
                    runner = runner.next
                cur.next = runner
                cur = runner
            return head

        :type head: ListNode
        :rtype: ListNode
        """
        uniq, fast = head, head.next

        while fast:
            if fast.val == uniq.val:
                uniq.next = fast.next
            else:
                uniq = fast
            fast = fast.next

        return head


if __name__ == "__main__":
    solution = Solution()
    l = create_list([])
    print(solution.deleteDuplicates(l))
