#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
86. Partition List

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/4
"""
from listnode import ListNode, create_list


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy_smaller, dummy_greater = ListNode(-1), ListNode(-1)
        smaller, greater = dummy_smaller, dummy_greater

        while head:
            if head.val < x:
                smaller.next = head
                smaller = smaller.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next

        smaller.next = dummy_greater.next
        greater.next = None

        return dummy_smaller.next

if __name__ == "__main__":
    solution = Solution()
    l = create_list([1, 4, 3, 2, 5, 2])
    print(l)
    print(solution.partition(l, 3))
