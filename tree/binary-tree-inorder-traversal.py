#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/2/27
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversalRecurisive(self, root):
        result = []
        self.inorderRecurisive(root, result)
        return result

    def inorderRecurisive(self, root, res):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            self.inorderRecurisive(root.left, res)
            res.append(root.val)
            self.inorderRecurisive(root.right, res)

    def inorderTraversalIterative(self, root):
        stack, res = [], []

        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right

    def morris_inorder_traversal(self, root):
        """
        Time: O(n), Space: O(1)
        步骤：
        1. 如果当前节点的左孩子为空，则输出当前节点并将其右孩子作为当前节点。
        2. 如果当前节点的左孩子不为空，在当前节点的左子树中找到当前节点在中序遍历下的前驱节点。
           a) 如果前驱节点的右孩子为空，将它的右孩子设置为当前节点。当前节点更新为当前节点的左孩子。
           b) 如果前驱节点的右孩子为当前节点，将它的右孩子重新设为空（恢复树的形状）。输出当前节点。
              当前节点更新为当前节点的右孩子。
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
                    current = current.left
                else:
                    node.right = None
                    result.append(current.val)
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
    print(Solution().inorderTraversalRecurisive(root))
    print(Solution().inorderTraversalIterative(root))
    print(Solution().morris_inorder_traversal(root))
