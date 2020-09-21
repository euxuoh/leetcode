#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
234. Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/11/26
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
    def ispalindrome_stack(self, head):
        """快慢指针找到中点，前半部分入栈
            Time: O(n)
            Space: O(n/2)
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        slow, fast = head, head
        stack = [head.val]
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            stack.append(slow.val)

        if not fast.next:
            stack.pop()

        while slow.next:
            slow = slow.next
            if stack.pop() != slow.val:
                return False

        return True

    def ispalindrome(self, head):
        """快慢指针找到中点，前半部分链表逆置
            Time: O(n)
            Space: O(1)
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        reverse, fast = None, head

        while fast and fast.next:
            fast = fast.next.next
            head.next, reverse, head = reverse, head, head.next

        tail = head.next if fast else head

        is_palindrome = True
        while reverse:
            is_palindrome = is_palindrome and reverse.val == tail.val
            reverse.next, head, reverse = head, reverse, reverse.next
            tail = tail.next

        return is_palindrome


if __name__ == "__main__":
    solution = Solution()
    test1 = create_list([1, 2, 3, 4, 3, 2, 1])
    test2 = create_list(range(10))
    # print test1
    # print test2
    # assert solution.ispalindrome(test1)
    # assert solution.ispalindrome_stack(test1)
    # assert not solution.ispalindrome(test2)
    # assert not solution.ispalindrome_stack(test2)
