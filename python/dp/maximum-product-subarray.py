#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
152. Maximum Product Subarray

Find the contiguous subarray within an array (containing
at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/19
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        数组为nums，因为可能存在负数，我们用Max来表示以nums[i]结尾的最大连续乘积值，
        用Min表示以nums[i]结尾的最小连续乘积值。状态转移方程为：
        Max[i] = max{nums[i], nums[i]*Max[i-1], nums[i]*Min[i-1]}
        Min[i] = min{nums[i], nums[i]*Max[i-1], nums[i]*Min[i-1]}
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        Max, Min = [0] * length, [0] * length
        result = Max[0] = Min[0] = nums[0]
        for i in range(1, length):
            Max[i] = max(max(nums[i], nums[i]*Max[i-1]), nums[i]*Min[i-1])
            Min[i] = min(min(nums[i], nums[i]*Max[i-1]), nums[i]*Min[i-1])
            result = max(result, Max[i])
        return result

    def max_product(self, nums):
        """
        优化空间复杂度
        :param nums:
        :return:
        """
        length = len(nums)
        if length == 0:
            return 0
        max_end, min_end, result = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            end1 = num * max_end
            end2 = num * min_end
            max_end = max(max(end1, end2), num)
            min_end = min(min(end1, end2), num)
            result = max(result, max_end)
        return result


if __name__ == "__main__":
    print(Solution().maxProduct([2, 3, -2, 4]))
    print(Solution().max_product([2, 3, -2, 4]))
