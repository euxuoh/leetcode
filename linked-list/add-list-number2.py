#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
445. Add Two Numbers II

You are given two linked lists representing two non-negative numbers.
The most significant digit comes first and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/6
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
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        array1, array2 = [], []
        while l1:
            array1.append(l1.val)
            l1 = l1.next
        while l2:
            array2.append(l2.val)
            l2 = l2.next

        prev, head = None, None
        carry = 0
        while array1 or array2:
            carry /= 10
            if array1:
                carry += array1.pop()
            if array2:
                carry += array2.pop()

            head = ListNode(carry % 10)
            head.next = prev
            prev = head

        if carry >= 10:
            head = ListNode(carry / 10)
            head.next = prev

        return head


if __name__ == "__main__":
    solution = Solution()
    l1 = create_list([7, 2, 4, 3])
    l2 = create_list([5, 6, 4])
    print(solution.addTwoNumbers(l1, l2))
