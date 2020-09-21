#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
16. 3Sum Closest

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/11/30
"""
from itertools import combinations


class Solution(object):
    def threeSumClosest(self, nums, target):
        """排列组合
            Time: O(n^3)    Time Limited Exceeded
            Space: O(1)
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        diff = float('inf')
        ans = 0

        for item in combinations(nums, 3):
            if abs(sum(item) - target) < diff:
                diff = abs(sum(item) - target)
                ans = sum(item)

        return ans

    def three_sum_closest(self, nums, target):
        """排列组合
            Time: O(n^3)    Time Limited Exceeded
            Space: O(1)
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = None

        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l < r:
                sums = nums[i] + nums[l] + nums[r]
                if ans is None or abs(sums-target) < abs(ans-target):
                    ans = sums
                if sums < target:
                    l += 1
                elif sums > target:
                    r -= 1
                else:
                    return ans

        return ans

    def three_sum_closest2(self, nums, target):
        nums, ans, min_diff = sorted(nums), float('inf'), float('inf')

        if sum(nums[-3:]) <= target:
            return sum(nums[-3:])

        if sum(nums[:3]) >= target:
            return sum(nums[:3])

        for i in range(len(nums)-2):
            if i == 0 or nums[i] != nums[i-1]:
                l, r = i+1, len(nums)-1
                while l < r:
                    diff = nums[i] + nums[l] + nums[r] - target
                    if abs(diff) < min_diff:
                        min_diff = abs(diff)
                        ans = nums[i] + nums[l] + nums[r]
                    if diff < 0:
                        l += 1
                    elif diff > 0:
                        r -= 1
                    else:
                        return target

        return ans

if __name__ == "__main__":
    solution = Solution()
    test_nums1 = [-1, 2, 1, -4]
    test_nums2 = range(10)
    assert solution.threeSumClosest(test_nums1, 1) == 2
    assert solution.threeSumClosest(test_nums2, 50) == 24

    assert solution.three_sum_closest(test_nums1, 1) == 2
    assert solution.three_sum_closest(test_nums2, 50) == 24

    assert solution.three_sum_closest2(test_nums1, 1) == 2
    assert solution.three_sum_closest2(test_nums2, 50) == 24
