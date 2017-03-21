#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
155. Min Stack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/20
"""


class MinStack(object):
    def __init__(self):
        self.stack, self.min_stack = [], []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        self.min_stack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]

if __name__ == "__main__":
    import random
    stack = MinStack()

    for i in range(10):
        stack.push(random.randint(1, 10))


