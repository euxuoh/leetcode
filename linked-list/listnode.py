#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/11/30
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

    def __str__(self):
        if self:
            return '{}'.format(self.val)
        else:
            return None

    # def __repr__(self):
    #     if self:
    #         return '{}->{}'.format(self.val, repr(self.next))


if __name__ == "__main__":
    print(create_list(range(10)))
