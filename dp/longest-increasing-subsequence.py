#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
300. 最长递增子序列

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/11
"""


class Solution(object):
    def length_of_LIS(self, nums):
        """traditional DP solution
        对于长度为N的数组A[N] = {a0, a1, a2, ..., an-1}，假设假设我们想求以aj结尾的最大递增子序列长度，
        设为L[j]，那么L[j] = max(L[i]) + 1, where i < j && a[i] < a[j], 也就是i的范围是0到j - 1。
        这样，想求aj结尾的最大递增子序列的长度，我们就需要遍历j之前的所有位置i（0到j-1），找出a[i] < a[j]，
        计算这些i中，能产生最大L[i]的i，之后就可以求出L[j]。

        之后我对每一个A[N]中的元素都计算以他们各自结尾的最大递增子序列的长度，这些长度的最大值，
        就是我们要求的问题——数组A的最大递增子序列。
        Time: O(n^2)
        Space: O(n)
        :param nums:
        :return:
        """
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)

        print(dp)

        return max(dp) if dp else 0

    def length_of_LIS_bisearch(self, nums):
        """二分搜索方法
        Time: O(n*log(n))
        Space: O(n)
        :param nums:
        :return:
        """
        import bisect
        LIS = []
        for num in nums:
            left = bisect.bisect_left(LIS, num)
            if left == len(LIS):
                LIS.append(num)
            else:
                LIS[left] = num
        return len(LIS)


if __name__ == "__main__":
    print(Solution().length_of_LIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(Solution().length_of_LIS_bisearch([10, 9, 2, 5, 3, 7, 101, 18]))