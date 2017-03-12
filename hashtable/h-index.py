#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
274. H-Index


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/29
"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        h_list = [0] * (n+1)
        for c in citations:
            if c >= n:
                h_list[n] += 1
            else:
                h_list[c] += 1

        print(h_list)

        h = 0
        for i in range(n, -1, -1):
            h += h_list[i]
            if h >= i:
                return i

    def h_index(self, citations):
        for i, c in enumerate(sorted(citations, reverse=True)):
            if i >= c:
                return i
        return len(citations)

    def h_index_sorted(self, citations):
        n = len(citations)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if citations[mid] >= n - mid:
                right = mid - 1
            else:
                left = mid + 1

        return n - left



if __name__ == "__main__":
    solution = Solution()
    print(solution.h_index([6, 6, 6, 8, 5, 1, 2]))
