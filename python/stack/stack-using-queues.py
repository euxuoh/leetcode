#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
225. Implement Stack using Queues

Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.

Note.
You must use only standard operations of a queue -- which means only
push to back, peek/pop from front, size, and is empty operations are valid.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/20
"""


class Queue(object):
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]

    def size(self):
        return len(self.data)

    def empty(self):
        return len(self.data) == 0


class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = Queue()
        self._top = None

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self._top = x
        self.queue.push(self.top)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        for _ in range(self.queue.size()-1):
            self._top = self.queue.pop()
            self.queue.push(self.top)
        return self.queue.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self._top

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.queue.empty()


if __name__ == "__main__":
    # Your MyStack object will be instantiated and called as such:
    obj = MyStack()
    obj.push(1)
    # param_2 = obj.pop()
    param_3 = obj.top()
    # param_4 = obj.empty()
