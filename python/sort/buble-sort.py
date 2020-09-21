#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/4
"""


class BubleSort(object):
    def buble_sort(self, nums):
        if len(nums) <= 1:
            return nums

        for i in range(len(nums)-1, 0, -1):
            for j in range(0, i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

    def buble_sort_flag(self, nums):
        if len(nums) <= 1:
            return nums

        n = len(nums) - 1
        while n > 0:
            pos = 0
            for j in range(0, n):
                if nums[j] > nums[j+1]:
                    pos = j
                    nums[j], nums[j+1] = nums[j+1], nums[j]
            n = pos

    def buble_sort_both_way(self, nums):
        n = len(nums)

        if n <= 1:
            return nums

        low, high = 0, n-1
        while low < high:
            for j in range(low, high):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
            high -= 1
            for j in range(high, low, -1):
                if nums[j] < nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
            low += 1

if __name__ == "__main__":
    import random
    l = [random.randint(1, 100) for _ in range(10)]
    print(l)
    BubleSort().buble_sort(l)
    # BubleSort().buble_sort_flag(l)
    # BubleSort().buble_sort_both_way(l)
    print(l)
