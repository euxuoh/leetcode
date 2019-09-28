#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
378. Kth Smallest Element in a Sorted Matrix

Given a n x n matrix where each of the rows and columns are sorted
in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not
the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/8
"""
import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import heapq

        rows, cols = len(matrix), len(matrix[0])
        min_heap = [(matrix[0][0], 0, 0)]
        visited = [[False] * cols for _ in range(rows)]
        visited[0][0] = True
        ans = None

        for _ in range(k):
            ans, i, j = heapq.heappop(min_heap)
            if (i+1) < rows and not visited[i+1][j]:
                heapq.heappush(min_heap, (matrix[i+1][j], i+1, j))
                visited[i+1][j] = True
            if (j+1) < cols and not visited[i][j+1]:
                heapq.heappush(min_heap, (matrix[i][j+1], i, j+1))
                visited[i][j+1] = True

        return ans

    def kth_smallest(self, matrix, k):
        rows, cols = len(matrix), len(matrix[0])
        min_heap = [(matrix[0][0], 0, 0)]
        ans = None

        for _ in range(k):
            ans, i, j = heapq.heappop(min_heap)
            if i < rows-1 and j == 0:
                heapq.heappush(min_heap, (matrix[i+1][j], i+1, j))
            if j < cols-1:
                heapq.heappush(min_heap, (matrix[i][j+1], i, j+1))

        return ans

    def kth_smallest_bin(self, matrix, k):
        """
        二分法查找
        :param matrix:
        :param k:
        :return:
        """
        import bisect

        lo, hi = matrix[0][0], matrix[-1][-1]

        while lo <= hi:
            mid = (lo + hi) // 2
            loc = sum(bisect.insort_right(m, mid) for m in matrix)
            if loc >= k:
                hi = mid - 1
            else:
                lo = mid + 1

        return lo


if __name__ == "__main__":
    print(Solution().kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
