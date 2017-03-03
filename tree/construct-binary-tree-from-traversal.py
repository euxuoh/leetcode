#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/1
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def build_tree_from_pre_inorder(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.build_tree_from_pre_inorder(preorder, inorder[:ind])
            root.right = self.build_tree_from_pre_inorder(preorder, inorder[ind+1:])
            return root

    def build_tree_from_in_postorder(self, inorder, postorder):
        if inorder:
            ind = inorder.index(postorder.pop())
            root = TreeNode(inorder[ind])
            root.right = self.build_tree_from_in_postorder(inorder[ind+1:], postorder)
            root.left = self.build_tree_from_in_postorder(inorder[:ind], postorder)
            return root


if __name__ == "__main__":
    pass
