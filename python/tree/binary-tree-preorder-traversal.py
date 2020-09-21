#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/2/27
"""


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversalRecursive(self, root):
        result = []
        self.preorderRecursive(root, result)
        return result

    def preorderRecursive(self, root, res):
        if root:
            res.append(root.val)
            self.preorderRecursive(root.left, res)
            self.preorderRecursive(root.right, res)

    def preorderTraversalIterative(self, root):
        result, stack = [], []
        while True:
            while root:
                result.append(root.val)
                stack.append(root)
                root = root.left
            if not stack:
                return result
            node = stack.pop()
            root = node.right

    def morris_preorder_traversal(self, root):
        """
        步骤：
        1. 如果当前节点的左孩子为空，则输出当前节点并将其右孩子作为当前节点。
        2. 如果当前节点的左孩子不为空，在当前节点的左子树中找到当前节点在中序遍历下的前驱节点。
           a) 如果前驱节点的右孩子为空，将它的右孩子设置为当前节点。
              输出当前节点（在这里输出，这是与中序遍历唯一一点不同）。当前节点更新为当前节点的左孩子。
           b) 如果前驱节点的右孩子为当前节点，将它的右孩子重新设为空。当前节点更新为当前节点的右孩子。
        3. 重复以上1、2直到当前节点为空。
        :param root:
        :return:
        """
        result, current = [], root

        while current:
            if current.left is None:
                result.append(current.val)
                current = current.right
            else:
                node = current.left
                while node.right and node.right != current:
                    node = node.right

                if node.right is None:
                    node.right = current
                    result.append(current.val)
                    current = current.left
                else:
                    node.right = None
                    current = current.right

        return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(6)
    root.left.left.right = TreeNode(7)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    print(Solution().preorderTraversalRecursive(root))
    print(Solution().preorderTraversalIterative(root))
    print(Solution().morris_preorder_traversal(root))
