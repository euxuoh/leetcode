#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
310. Minimum Height Trees

For a undirected graph with tree characteristics, we can choose
any node as the root. The result graph is then a rooted tree.
Among all possible rooted trees, those with minimum height are
called minimum height trees (MHTs). Given such a graph, write a f
unction to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1.
You will be given the number n and a list of undirected edges
(each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0, 1] is the same as [1, 0]
and thus will not appear together in edges.

Example 1:

Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3
return [1]

Example 2:

Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5
return [3, 4]

Show Hint
Note:

(1) According to the definition of tree on Wikipedia: “a tree is
an undirected graph in which any two vertices are connected by
exactly one path. In other words, any connected graph without
simple cycles is a tree.”

(2) The height of a rooted tree is the number of edges on the longest
downward path between the root and a leaf.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/23
"""


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """逐层删掉叶子结点, 直到剩下根节点为止
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict
        children = defaultdict(set)
        for edge in edges:
            children[edge[0]].add(edge[1])
            children[edge[1]].add(edge[0])
        vertices = set(children.keys())
        while len(vertices) > 2:
            leaves = [x for x in children if len(children[x]) == 1]
            for leave in leaves:
                for child in children[leave]:
                    children[child].remove(leave)
                del children[leave]
                vertices.remove(leave)
        return list(vertices) if n != 1 else [0]


if __name__ == "__main__":
    print(Solution().findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))
