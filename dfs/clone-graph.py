#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
133. Clone Graph

Clone an undirected graph. Each node in the graph contains a label
 and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node
label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three
parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.

Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/4/3
"""


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    def cloneGraph(self, node):
        """dfs遍历图，利用字典维护标号和新增节点之间的映射关系
        :param node: undirected graph node
        :return: a undirected graph node
        """
        if node is None:
            return None

        needle = UndirectedGraphNode(node.label)
        node_dict = {node.label: needle}
        stack = [node]

        while stack:
            top = stack.pop()
            cnode = node_dict[top.label]
            for n in top.neighbors:
                if n.label not in node_dict:
                    node_dict[n.label] = UndirectedGraphNode(n.label)
                    stack.append(n)
                cnode.neighbors.append(node_dict[n.label])

        return needle


if __name__ == "__main__":
    pass
