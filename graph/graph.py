#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

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

    def find_path(self, start, end, path=[]):
        """回溯法寻找路径
        :param start:
        :param end:
        :param path:
        :return:
        """
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph:
            return None
        for node in self.graph[start]:
            if node not in path:
                new_path = self.find_path(node, end, path)
                if new_path:
                    return new_path
        return None

    def find_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph:
            return []
        paths = []
        for node in self.graph[start]:
            if node not in path:
                new_paths = self.find_all_paths(node, end, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths

    def find_shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph:
            return None
        shortest_path = None
        for node in self.graph[start]:
            if node not in path:
                new_path = self.find_shortest_path(node, end, path)
                if new_path:
                    if not shortest_path or len(new_path) < len(shortest_path):
                        shortest_path = new_path
        return shortest_path

    def erase_visited(self):
        for node in self.visited:
            self.visited[node] = False

    def dfs_traversal(self, root=None):
        self.erase_visited()
        order = []

        def dfs(node):
            self.visited[node] = True
            order.append(node)
            for n in self.graph[node]:
                if not self.visited[n]:
                    dfs(n)

        if root:
            dfs(root)
        for node in self.graph.keys():
            if not self.visited[node]:
                dfs(node)

        return order

    def bfs_traversal(self, root=None):
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

        if root:
            queue.append(root)
            order.append(root)
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
    print(g.find_path('a', 'd'))
    print(g.find_all_paths('a', 'd'))
    print(g.find_shortest_path('a', 'd'))
    print(g.dfs_traversal('a'))
    print(g.bfs_traversal('a'))
