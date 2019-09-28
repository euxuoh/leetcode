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
    @staticmethod
    def bin_search(nums, target):
        if not nums:
            return -1
        left = bisect.bisect_left(nums, target)
        return -1 if left == len(nums) or nums[left] != target else left

    @staticmethod
    def bs_strict_lower_bound(nums, target):
        if not nums:
            return -1
        left = bisect.bisect_left(nums, target)
        return left-1

    @staticmethod
    def bs_strict_upper_bound(nums, target):
        if not nums:
            return -1
        right = bisect.bisect_right(nums, target)
        return -1 if right == len(nums) else right

    @staticmethod
    def bs_unstrict_lower_bound(nums, target):
        if not nums:
            return -1
        left = bisect.bisect_left(nums, target)
        return left-1 if left == len(nums) or nums[left] != target else left

    @staticmethod
    def bs_unstrict_upper_bound(nums, target):
        if not nums:
            return -1
        right = bisect.bisect_right(nums, target)
        if nums[right-1] == target:
            return right-1
        else:
            return -1 if right == len(nums) else right

    @staticmethod
    def search_range(nums, target):
        if not nums:
            return [-1, -1]
        left = bisect.bisect_left(nums, target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        right = bisect.bisect_right(nums, target)
        return [left, right - 1]


if __name__ == "__main__":
    test_nums = [2, 3, 5, 7]

    # 基本查找
    assert BinSearch().bin_search(test_nums, 1) == -1
    assert BinSearch().bin_search(test_nums, 2) == 0
    assert BinSearch().bin_search(test_nums, 3) == 1
    assert BinSearch().bin_search(test_nums, 4) == -1
    assert BinSearch().bin_search(test_nums, 7) == 3
    assert BinSearch().bin_search(test_nums, 8) == -1

    # 严格下界
    assert BinSearch().bs_strict_lower_bound(test_nums, 1) == -1
    assert BinSearch().bs_strict_lower_bound(test_nums, 2) == -1
    assert BinSearch().bs_strict_lower_bound(test_nums, 3) == 0
    assert BinSearch().bs_strict_lower_bound(test_nums, 4) == 1
    assert BinSearch().bs_strict_lower_bound(test_nums, 7) == 2
    assert BinSearch().bs_strict_lower_bound(test_nums, 8) == 3

    # 严格上界
    assert BinSearch().bs_strict_upper_bound(test_nums, 1) == 0
    assert BinSearch().bs_strict_upper_bound(test_nums, 2) == 1
    assert BinSearch().bs_strict_upper_bound(test_nums, 3) == 2
    assert BinSearch().bs_strict_upper_bound(test_nums, 4) == 2
    assert BinSearch().bs_strict_upper_bound(test_nums, 7) == -1
    assert BinSearch().bs_strict_upper_bound(test_nums, 8) == -1

    # 宽松下界
    assert BinSearch().bs_unstrict_lower_bound(test_nums, 1) == -1
    assert BinSearch().bs_unstrict_lower_bound(test_nums, 2) == 0
    assert BinSearch().bs_unstrict_lower_bound(test_nums, 3) == 1
    assert BinSearch().bs_unstrict_lower_bound(test_nums, 4) == 1
    assert BinSearch().bs_unstrict_lower_bound(test_nums, 7) == 3
    assert BinSearch().bs_unstrict_lower_bound(test_nums, 8) == 3

    # 宽松上界
    assert BinSearch().bs_unstrict_upper_bound(test_nums, 1) == 0
    assert BinSearch().bs_unstrict_upper_bound(test_nums, 2) == 0
    assert BinSearch().bs_unstrict_upper_bound(test_nums, 3) == 1
    assert BinSearch().bs_unstrict_upper_bound(test_nums, 4) == 2
    assert BinSearch().bs_unstrict_upper_bound(test_nums, 7) == 3
    assert BinSearch().bs_unstrict_upper_bound(test_nums, 8) == -1
