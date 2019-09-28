#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/4/9
"""
import sys


class Solution(object):
    def reverseWords(self, s):
        """
        :param s: String
        :return: String
        """
        if not s:
            return ''

        result = []
        s_list = map(list, s.split())
        for word in s_list:
            result.append(''.join(reversed(word)))
        return ' '.join(result)

    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        matrix = [[] for _ in range(len(wall))]
        for i, row in enumerate(wall):
            for brick in row:
                matrix[i].extend([1] * (brick-1) + [0])

        print(matrix)

        cnt = sys.maxsize
        rows, cols = len(matrix), len(matrix[0])
        for col in range(cols-1):
            sums = 0
            for row in range(rows):
                sums += matrix[row][col]
            cnt = min(cnt, sums)

        return len(matrix) if cnt == sys.maxsize else cnt

    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        pass


if __name__ == "__main__":
    # print(Solution().reverseWords("Let's take LeetCode contest"))
    print(Solution().leastBricks([[1, 2, 2, 1],
                                  [3, 1, 2],
                                  [1, 3, 2],
                                  [2, 4],
                                  [3, 1, 2],
                                  [1, 3, 1, 1]]))
