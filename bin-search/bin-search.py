#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/4/11
"""
import bisect


class BinSearch(object):
    def bin_search(self, nums, target, lo=0, hi=None):
        """基本实现
        不存在则返回-1
        :param nums:
        :param target:
        :param lo:
        :param hi:
        :return:
        """
        if lo < 0:
            raise ValueError('lo must be non-negative')
        if hi is None:
            hi = len(nums)-1

        while lo <= hi:
            mid = (lo+hi) >> 1
            if nums[mid] > target:
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                return mid

        return -1

    def bs_strict_lower_bound(self, nums, target, lo=0, hi=None):
        """
        查找严格下界
        :param nums:
        :param target:
        :param lo:
        :param hi:
        :return:
        """
        if lo < 0:
            raise ValueError('lo must be non-negative')
        if hi is None:
            hi = len(nums)

        while lo < hi:
            mid = (hi+lo) >> 1
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid

        return lo-1

    def bs_unstrict_lower_bound(self, nums, target, lo=0, hi=None):
        """
        查找非严格下界
        :param nums:
        :param target:
        :param lo:
        :param hi:
        :return:
        """
        if lo < 0:
            raise ValueError('lo must be non-negative')
        if hi is None:
            hi = len(nums)

        while lo < hi:
            mid = (hi + lo) >> 1
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid

        return lo-1 if lo == len(nums) or nums[lo] != target else lo

    def bs_strict_upper_bound(self, nums, target, lo=0, hi=None):
        """
        查找严格上界
        :param nums:
        :param target:
        :param lo:
        :param hi:
        :return:
        """
        if lo < 0:
            raise ValueError('lo must be non-negative')
        if hi is None:
            hi = len(nums)

        while lo < hi:
            mid = (hi+lo) >> 1
            if nums[mid] > target:
                hi = mid
            else:
                lo = mid + 1

        return -1 if lo == len(nums) else lo

    def bs_unstrict_upper_bound(self, nums, target, lo=0, hi=None):
        """
        查找非严格上界
        :param nums:
        :param target:
        :param lo:
        :param hi:
        :return:
        """
        if lo < 0:
            raise ValueError('lo must be non-negative')
        if hi is None:
            hi = len(nums)

        while lo < hi:
            mid = (hi+lo) >> 1
            if nums[mid] > target:
                hi = mid
            else:
                lo = mid + 1

        if nums[lo-1] == target:
            return lo-1
        else:
            return -1 if lo == len(nums) else lo

    def search_range(self, nums, target):
        """若数组中包含重复元素，查找target range
        :param nums:
        :param target:
        :return:
        """
        left = bisect.bisect_left(nums, target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        right = bisect.bisect_right(nums, target)
        return [left, right-1]


if __name__ == "__main__":
    test_nums = [2, 2, 3, 5, 7]

    # 基本查找
    # assert BinSearch().bin_search(test_nums, 1) == -1
    # assert BinSearch().bin_search(test_nums, 2) == 0
    # assert BinSearch().bin_search(test_nums, 3) == 1
    # assert BinSearch().bin_search(test_nums, 4) == -1
    # assert BinSearch().bin_search(test_nums, 7) == 3
    # assert BinSearch().bin_search(test_nums, 8) == -1

    # 严格下界
    # assert BinSearch().bs_strict_lower_bound(test_nums, 1) == -1
    # assert BinSearch().bs_strict_lower_bound(test_nums, 2) == 0
    # assert BinSearch().bs_strict_lower_bound(test_nums, 3) == 2
    # assert BinSearch().bs_strict_lower_bound(test_nums, 4) == -1
    # assert BinSearch().bs_strict_lower_bound(test_nums, 7) == 4
    # assert BinSearch().bs_strict_lower_bound(test_nums, 8) == -1

    # 严格上界
    # assert BinSearch().bs_strict_upper_bound(test_nums, 1) == 0
    # assert BinSearch().bs_strict_upper_bound(test_nums, 2) == 1
    # assert BinSearch().bs_strict_upper_bound(test_nums, 3) == 2
    # assert BinSearch().bs_strict_upper_bound(test_nums, 4) == 2
    # assert BinSearch().bs_strict_upper_bound(test_nums, 7) == -1
    # assert BinSearch().bs_strict_upper_bound(test_nums, 8) == -1

    # 宽松下界
    assert BinSearch().bs_unstrict_lower_bound(test_nums, 1) == -1
    assert BinSearch().bs_unstrict_lower_bound(test_nums, 2) == 0
    assert BinSearch().bs_unstrict_lower_bound(test_nums, 3) == 2
    assert BinSearch().bs_unstrict_lower_bound(test_nums, 4) == -1
    assert BinSearch().bs_unstrict_lower_bound(test_nums, 7) == 4
    assert BinSearch().bs_unstrict_lower_bound(test_nums, 8) == -1

    # 宽松上界
    # assert BinSearch().bs_unstrict_upper_bound(test_nums, 1) == 0
    # assert BinSearch().bs_unstrict_upper_bound(test_nums, 2) == 0
    # assert BinSearch().bs_unstrict_upper_bound(test_nums, 3) == 1
    # assert BinSearch().bs_unstrict_upper_bound(test_nums, 4) == 2
    # assert BinSearch().bs_unstrict_upper_bound(test_nums, 7) == 3
    # assert BinSearch().bs_unstrict_upper_bound(test_nums, 8) == -1
