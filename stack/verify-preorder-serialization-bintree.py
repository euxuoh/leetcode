#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
331. Verify Preorder Serialization of a Binary Tree

One way to serialize a binary tree is to use pre-order traversal.
When we encounter a non-null node, we record the node's value. If
it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string
"9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a
correct preorder traversal serialization of a binary tree. Find
an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer
or a character '#' representing null pointer.

You may assume that the input format is always valid, for example
it could never contain two consecutive commas such as "1,,3".

Example 1:
"9,3,4,#,#,1,#,#,2,#,6,#,#"
Return true

Example 2:
"1,#"
Return false

Example 3:
"9,#,#,1"
Return false

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/20
"""


class Solution(object):
    def isValidSerialization(self, preorder):
        """
        将元素压入栈
        如果当前栈的深度≥3，并且最顶端两个元素为'#', '#'，而第三个元素不为'#'，
        则将这三个元素弹出栈顶，然后向栈中压入一个'#'，重复此过程
        最后判断栈中剩余元素是否只有一个'#'
        :type preorder: str
        :rtype: bool
        """
        stack = []
        for e in preorder.split(','):
            stack.append(e)
            while len(stack) >= 3 and stack[-1] == stack[-2] == '#' and stack[-3] != '#':
                stack.pop(), stack.pop(), stack.pop()
                stack.append('#')
        return len(stack) == 1 and stack[0] == '#'

    def is_valid_serialization(self, preorder):
        """
        在二叉树中，如果我们将空节点视为叶子节点，那么除根节点外的非空节点（分支节点）提供2个出度
        和1个入度（2个孩子和1个父亲）, 所有的空节点提供0个出度和1个入度（0个孩子和1个父亲）
        假如我们尝试重建这棵树。在构建的过程中，记录出度与入度之差，记为diff = outdegree - indegree
        当遍历节点时，我们令diff - 1（因为节点提供了一个入度）。如果节点非空，再令diff + 2（因为节点提供了2个出度）
        如果序列化是正确的，那么diff在任何时刻都不会小于0，并且最终结果等于0

        对该算法的一个朴素理解：
        如果在遍历过程中的某时刻，系统的入度>出度，则说明当前序列中出现过的所有分支节点的“空闲分支”均已用完，
        后序节点没有办法挂载到之前出现的节点之上，从而判定先序遍历的序列是不合法的。
        :param preorder:
        :return:
        """
        diff = 1
        for e in preorder.split(','):
            diff -= 1
            if diff < 0:
                return False
            if e != '#':
                diff += 2
        return diff == 0


if __name__ == "__main__":
    print(Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
    print(Solution().is_valid_serialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
