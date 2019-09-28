#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
112. path sum i
113. path sum ii
437. path sum iii

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
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        if not root.left and not root.right and root.val == sum:
            return True

        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

    def pathSum(self, root, sum):
        if root is None:
            return []

        if not root.left and not root.right:
            if root.val == sum:
                return [[root.val]]
            else:
                return []

        a = self.pathSum(root.left, sum-root.val) + self.pathSum(root.right, sum-root.val)

        return [[root.val] + i for i in a]

    def all_path_sum(self, root, sum):
        """计算所有和为给定值的路径个数。路径不一定以根开始，
        也不一定以叶子结束，但是必须自上而下（从双亲结点到孩子节点）

        Solution: 树的遍历，在遍历节点的同时，以经过的节点为根，寻找子树中和为sum的路径
        :param root:
        :param sum:
        :return:
        """
        def traverse(root, val):
            if root is None:
                return 0
            res = (val == root.val)
            res += traverse(root.left, val-root.val)
            res += traverse(root.right, val-root.val)
            return res

        if root is None:
            return 0

        ans = traverse(root, sum)
        ans += self.all_path_sum(root.left, sum)
        ans += self.all_path_sum(root.right, sum)
        return ans


if __name__ == "__main__":
    root = TreeNode(10)
    root.left, root.right = TreeNode(5), TreeNode(-3)

    root.left.left, root.left.right = TreeNode(3), TreeNode(2)
    root.right.right = TreeNode(11)

    root.left.left.left, root.left.left.right = TreeNode(3), TreeNode(-2)
    root.left.right.right = TreeNode(1)

    print(Solution().all_path_sum(root, 8))
