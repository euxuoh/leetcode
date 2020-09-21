#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
436. Find Right Interval

Given a set of intervals, for each of the interval i, check if there exists an
interval j whose start point is bigger than or equal to the end point of the
interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which
means that the interval j has the minimum start point to build the "right"
relationship for interval i. If the interval j doesn't exist, store -1 for the
interval i. Finally, you need output the stored value of each interval as an
array.

Note:
You may assume the interval's end point is always bigger than its start point.
You may assume none of these intervals have the same start point.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/9
"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        import bisect
        res = []
        sorted_start = sorted((e.start, i) for i, e in enumerate(intervals))
        for e in intervals:
            pos = bisect.bisect_left(sorted_start, (e.end, ))
            res.append(sorted_start[pos][1] if pos < len(sorted_start) else -1)
        return res


if __name__ == "__main__":
    print(Solution().findRightInterval([Interval(1, 4), Interval(2, 3), Interval(3, 4)]))
