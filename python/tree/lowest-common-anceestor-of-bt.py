#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
235. Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two
given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is
defined between two nodes v and w as the lowest node in T that has both v and
w as descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another
example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself
according to the LCA definition.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/2/28
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    二叉搜索树中两节点的最低公共祖先
    """
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if p.val < root.val > q.val:
                root = root.left
            elif p.val > root.val < q.val:
                root = root.right
            else:
                return root

    def lower_common_ancestor_recursive(self, root, p, q):
        if p.val < root.val > q.val:
            return self.lower_common_ancestor_recursive(root.left, p, q)
        if p.val > root.val < q.val:
            return self.lower_common_ancestor_recursive(root.right, p, q)
        return root


class Solution2(object):
    """
    普通二叉树中两节点的最低公共祖先
    """
    def lowestCommonAncestor(self, root, p, q):
        if root in (None, p, q):
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left if left else right

    def lowest_common_ancestor(self, root, p, q):
        """
        1. 自顶向下找到p, q的父节点, 父节点的父节点, ......, 保存在parents字典中
        2. 自底向上找出p, q的祖先节点
        :param root:
        :param p:
        :param q:
        :return:
        """
        stack = [root]
        parents = {root: None}

        while p not in parents or q not in parents:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                parents[node.left] = node
            if node.right:
                stack.append(node.right)
                parents[node.right] = node

        ancestor = set()
        while p:
            ancestor.add(p)
            p = parents[p]
        while q not in ancestor:
            q = parents[q]

        return q


class Solution3(object):
    """
    树中两节点的最低公共祖先
    """
    def lowestCommonAncestor(self, root, p, q):
        pass


if __name__ == "__main__":
    pass
