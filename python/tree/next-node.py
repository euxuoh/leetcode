#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
剑指offer：58

给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/9/23
"""


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution(object):
    def next_node(self, node):
        """
        1)	给定的节点有右孩子，就是右子树的最左孩子；
        2)	给定的节点没有右孩子:
                a.如果给定节点是父节点的左孩子，直接返回父节点，
                b.如果给定节点是父节点的右孩子，那么拿父节点作为当前节点去向上递归，
                  直到当前节点没有父节点返回null，或者当前节点是父节点的左孩子，返回父节点
        :param node:
        :return:
        """
        if node is None:
            return None

        if node.right:
            # 返回右子树的最左孩子
            self.mostleft_child_in_right_tree(node.right)
        else:
            #
            self.next_in_parent(node)

    def mostleft_child_in_right_tree(self, node):
        if node.left is None:
            return node
        else:
            return self.mostleft_child_in_right_tree(node.left)

    def next_in_parent(self, node):
        if node.parent and node.parent.left is node:
            return node.parent
        elif node.parent and node.parent.right is node:
            self.next_in_parent(node.parent)
        else:
            return None


if __name__ == "__main__":
    pass
