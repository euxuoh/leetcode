#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
142. Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/4
"""
from .listnode import ListNode, create_list


class Solution(object):
    def detectCycle(self, head):
        """假设head到entry的距离为L1, entry到meeting的距离为L2，环的长度为C
        第一次相遇时，fast走过的距离是L1 + n * C + L2
                    slow走过的距离是L1 + L2
        又因为，fast走过的距离是slow的两倍，可得：L1 = n * C - L2 = (n-1) * C + (C - L2)
        (n-1) * C相当于回到原点，即为0，所以L1 = C - L2, 即head到entry的距离等于meeting到entry的正向距离

        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                fast = head
                while fast is not slow:
                    slow, fast = slow.next, fast.next
                return fast

        return None


if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = head.next
    print(solution.detectCycle(head))
