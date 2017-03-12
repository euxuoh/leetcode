#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/5
"""


class InsertionSort(object):
    def insertion_sort(self, nums):
        if len(nums) <= 1:
            return nums

        for i in range(0, len(nums)):
            for j in range(i, 0, -1):
                if nums[j] < nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]

        return nums

if __name__ == "__main__":
    import random

    l = [random.randint(0, 100) for _ in range(10)]
    print(InsertionSort().insertion_sort(l))

