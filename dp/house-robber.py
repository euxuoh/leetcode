#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
198. House Robber

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/15
"""


class Solution(object):
    def houseRobber(self, nums):
        """
        动态转移方程：dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        dp[i]表示打劫到第i家的时候，累计取得的金钱最大值
        :param nums:
        :return:
        """
        size = len(nums)
        dp = [0] * (size + 1)
        if size:
            dp[1] = nums[0]
        for i in range(2, size+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
        return dp[size]

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
