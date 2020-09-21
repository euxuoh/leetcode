#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
207. Course Schedule

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have
to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it
possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have
finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have
finished course 0, and to take course 0 you should also have finished
course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not
adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/23
"""


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """拓扑排序判断有向图是否有环
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = [0] * numCourses
        adjacency = [[] for _ in range(numCourses)]
        for pair in prerequisites:
            indegree[pair[0]] += 1
            adjacency[pair[1]].append(pair[0])
        courses = set(range(numCourses))
        flag = True
        while flag and len(courses):
            flag = False
            remove_list = []
            for x in courses:
                if indegree[x] == 0:
                    for n in adjacency[x]:
                        indegree[n] -= 1
                    remove_list.append(x)
                    flag = True
            for x in remove_list:
                courses.remove(x)
        return len(courses) == 0


if __name__ == "__main__":
    print(Solution().canFinish(2, [[1, 0]]))
    print(Solution().canFinish(2, [[1, 0], [0, 1]]))
