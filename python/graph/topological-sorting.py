#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
拓扑排序

在图论中，由一个有向无环图的顶点组成的序列，当且仅当满足下列条件时，称为该图的一个拓扑排序
1.每个顶点出现且只出现一次；
2.若A在序列中排在B的前面，则在图中不存在从B到A的路径。

也可以定义为：拓扑排序是对有向无环图的顶点的一种排序，它使得如果存在一条从顶点A到顶点B的路径，
那么在排序中B出现在A的后面。

一个有向图能被拓扑排序的充要条件就是它是一个有向无环图(DAG)
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

    def get_edges(self):
        edges = []
        for node, neighbors in self.graph.items():
            for neighbor in neighbors:
                edges.append((node, neighbor))
        return edges

    def toposort_kahn(self):
        nodes = list(self.graph.keys())
        edges = self.get_edges()
        result = []

        def indegree_zero(v, es):
            """
            删除入度为0的节点和相关的边
            :param v: 节点结合
            :param es: 边集合
            :return: 入度为0的节点
            """
            if not v:
                return None
            zero_indegree = v[:]
            for e in es:
                if e[1] in zero_indegree:
                    zero_indegree.remove(e[1])
            if not zero_indegree:
                return -1
            for n in zero_indegree:
                for i, e in enumerate(es):
                    if n in e:
                        es[i] = ''
            if es:
                es[:] = [x for x in es if x]
            if v:
                v[:] = [x for x in v if x not in zero_indegree]
            return zero_indegree

        while True:
            indegree_zero_nodes = indegree_zero(nodes, edges)
            if not indegree_zero_nodes:
                break
            if indegree_zero_nodes == -1:
                print("There is a circle.")
                return None
            result.extend(indegree_zero_nodes)
        return result

    def erase_visited(self):
        for node in self.visited:
            self.visited[node] = False

    def toposort_dfs(self, start=None):
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
            for n in self.graph[node]:
                if not self.visited[n]:
                    dfs(n)
            order.append(node)

        if start:
            dfs(start)
        for node in self.graph.keys():
            if not self.visited[node]:
                dfs(node)

        return order[::-1]

if __name__ == "__main__":
    g = Graph(['a', 'b', 'c', 'd', 'e', 'f'])
    g.add_edges([('a', 'b'), ('a', 'c'), ('b', 'c'), ('b', 'd'), ('c', 'd'), ('d', 'c'), ('e', 'f'), ('f', 'c')])
    print(g.toposort_dfs('a'))
