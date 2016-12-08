#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
206. Reverse Linked List

Reverse a singly linked list.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/4
"""
from listnode import ListNode, create_list


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(float('-inf'))
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next

    def reverse_list_recu(self, head):
        """递归版本，好难理解啊，23333.。。
        :type head: ListNode
        :rtype: ListNode
        """
        [begin, _] = self.recursion(head)
        return begin

    def recursion(self, head):
        if not head:
            return [None, None]

        [begin, end] = self.recursion(head.next)

        if end:
            end.next = head
            head.next = None
            return [begin, head]
        else:
            return [head, head]


if __name__ == "__main__":
    solution = Solution()
    l = create_list(range(10))
    print(solution.reverseList(l))
    print(solution.reverse_list_recu(create_list(range(10))))
