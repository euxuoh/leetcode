#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
328. Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and
O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/7
"""
from listnode import ListNode, create_list


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        odd = odd_head = ListNode(-1)
        even = even_head = ListNode(-1)

        while head:
            odd.next = head
            odd = odd.next
            even.next = head.next
            even = even.next

            head = head.next.next if head.next else None

        odd.next = even_head.next
        if even:
            even.next = None

        return odd_head.next


if __name__ == "__main__":
    solution = Solution()
    l = create_list([range(10)])
    print(solution.oddEvenList(l))
