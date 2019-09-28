#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
图的遍历

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/22
"""
from collections import defaultdict


class Graph(object):
    def __init__(self, node_list):
        self.graph = defaultdict(list)
        self.visited = {}
        self.add_nodes(node_list)

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []
            self.visited[node] = False

    def add_nodes(self, node_list):
        for node in node_list:
            self.add_node(node)

    def add_edge(self, edge):
        start, end = edge
        self.graph[start].append(end)

    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge)

    def erase_visited(self):
        for node in self.visited:
            self.visited[node] = False

    def dfs_traversal(self, start=None):
        """
        1. 访问初始结点v，并标记结点v为已访问。
        2. 查找结点v的第一个邻接结点w。
        3. 若w存在，则继续执行4，否则算法结束。
        4. 若w未被访问，对w进行深度优先遍历递归（即把w当做另一个v，然后进行步骤123）。
        5. 查找结点v的w邻接结点的下一个邻接结点，转到步骤3。
        :param start:
        :return:
        """
        self.erase_visited()
        order = []

        def dfs(node):
            self.visited[node] = True
            order.append(node)
            for n in self.graph[node]:
                if not self.visited[n]:
                    dfs(n)

        if start:
            dfs(start)
        for node in self.graph.keys():
            if not self.visited[node]:
                dfs(node)

        return order

    def bfs_traversal(self, start=None):
        """
        1. 访问初始结点v并标记结点v为已访问。
        2. 结点v入队列
        3. 当队列非空时，继续执行，否则算法结束。
        4. 出队列，取得队头结点u。
        5. 查找结点u的第一个邻接结点w。
        6. 若结点u的邻接结点w不存在，则转到步骤3；否则循环执行以下三个步骤：
            1). 若结点w尚未被访问，则访问结点w并标记为已访问。
            2). 结点w入队列
            3). 查找结点u的继w邻接结点后的下一个邻接结点w，转到步骤6。
        :param start:
        :return:
        """
        self.erase_visited()
        queue, order = [], []

        def bfs():
            while queue:
                node = queue.pop(0)
                self.visited[node] = True
                for n in self.graph[node]:
                    if not self.visited[n] and n not in queue:
                        queue.append(n)
                        order.append(n)

        if start:
            queue.append(start)
            order.append(start)
            bfs()
        for node in self.graph.keys():
            if not self.visited[node]:
                queue.append(node)
                order.append(node)
                bfs()
        return order

if __name__ == "__main__":
    g = Graph(['a', 'b', 'c', 'd', 'e', 'f'])
    g.add_edges([('a', 'b'), ('a', 'c'), ('b', 'c'), ('b', 'd'), ('c', 'd'), ('d', 'c'), ('e', 'f'), ('f', 'c')])
    print(g.dfs_traversal('a'))
    print(g.bfs_traversal('a'))
