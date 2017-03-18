#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
198. House Robber

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/15
"""


class Solution(object):
    def house_robber(self, nums):
        """

        :param nums:
        :return:
        """
        last, now = 0, 0
        for num in nums:
            last, now = now, max(last+num, now)
        return now

if __name__ == "__main__":
    print(Solution().house_robber([0, 9, 9, 9, 9, 9, 1]))
