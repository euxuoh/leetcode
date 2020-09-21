#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/9/23
"""


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def serialize(self, root):
        if not root:
            return '[]'
        result = [root.val]
        queue = [root]

        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            result.append(node.left.val if node.left else 'null')
            result.append(node.right.val if node.right else 'null')

        while result and result[-1] == 'null':
            result.pop()

        return '[' + ','.join(map(str, result)) + ']'

    def deserialize(self, data):
        if data == '[]':
            return None
        nodes, queue = [], []

        for e in data[1:-1].split(','):
            if e == 'null':
                nodes.append(None)
            else:
                nodes.append(TreeNode(e))

        queue.append(nodes.pop(0) if nodes else None)
        root = queue[0] if queue else None

        while queue:
            parent = queue.pop(0)
            left = nodes.pop(0) if nodes else None
            right = nodes.pop(0) if nodes else None
            parent.left, parent.right = left, right
            if left:
                queue.append(left)
            if right:
                queue.append(right)

        return root


if __name__ == "__main__":
    pass
