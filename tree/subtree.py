#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
剑指offer18

输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/9/23
"""


class Solution(object):
    def is_subtree(self, root1, root2):
        """
        比较两个节点root1，root2的值是否相等，如果相等，那么进入subtree函数，
        依次比较左右子树是否完全相同，
        如果左右子树都完全相同，那么返回true，不完全相同的话返回false，
        再分别比较root1.Left和root2，root1.right和root2
        :param t1:
        :param t2:
        :return:
        """
        if root1 is None or root2 is None:
            return False
        res = False
        if root1.val == root2.val:
            res = self.dose_tree1_have_tree2(root1, root2)
        if not res:
            res = self.is_subtree(root1.left, root2)
        if not res:
            res = self.is_subtree(root1.right, root2)

        return res

    def dose_tree1_have_tree2(self, root1, root2):
        if root2 is None:
            return True
        if root1 is None:
            return False
        if root1.val != root2.val:
            return False

        return self.dose_tree1_have_tree2(root1.left, root2.left) and \
            self.dose_tree1_have_tree2(root1.right, root2.right)


if __name__ == "__main__":
    pass
