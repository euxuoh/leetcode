#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/5
"""


class ListNode(object):
    def __init__(self, val):
        self.data = val
        self.next = None


class BucketSort(object):
    def __init__(self):
        self.bucket_num = 10

    def insert(self, head, val):
        node = ListNode(val)

        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head

        while cur and cur.data <= val:
            pre = cur
            cur = cur.next
        pre.next, node.next = node, cur

        return dummy.next

    def merge(self, head1, head2):
        cur = dummy = ListNode(-1)

        while head1 and head2:
            if head1.data <= head2.data:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next

        cur.next = head1 or head2

        return dummy.next

    def bucket_sort(self, nums):
        if len(nums) <= 1:
            return nums

        buckets = [ListNode(0) for _ in range(self.bucket_num)]

        for n in nums:
            head = buckets[n//self.bucket_num]
            buckets[n//self.bucket_num] = self.insert(head, n)

        head = buckets[0].next
        for i in range(1, self.bucket_num):
            head = self.merge(head, buckets[i].next)

        for i in range(len(nums)):
            nums[i] = head.data
            head = head.next

        return nums


if __name__ == "__main__":
    import random

    l = [random.randint(0, 99) for _ in range(10)]
    print(BucketSort().bucket_sort(l))

