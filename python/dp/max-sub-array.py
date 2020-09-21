#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
max sub-array sum

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/14
"""


class Solution(object):
    def max_sub_array(self, nums):
        """最大子数组和
        我们令currSum为当前最大子数组的和，maxSum为最后要返回的最大子数组的和。
        当我们往后扫描时，对第j+1个元素有两种选择：要么放入前面找到的子数组，要么做为新子数组的第一个元素；
        如果currSum加上当前元素a[j]后不小于a[j]，则令currSum加上a[j]，
        否则currSum重新赋值，置为下一个元素，即currSum = a[j]。
        同时，当currSum > maxSum，则更新maxSum = currSum，否则保持原值，不更新。
        即
            currSum = max(a[j], currSum + a[j])
            maxSum = max(maxSum, currSum)
        :param nums:
        :return:
        """
        curr_sum, max_sum = 0, nums[0]

        for num in nums:
            curr_sum = max(curr_sum + num, num)
            max_sum = max(max_sum, curr_sum)

        return max_sum

if __name__ == "__main__":
    print(Solution().max_sub_array([-1, -2, -3, -10, -4, -7, -2, -5]))
