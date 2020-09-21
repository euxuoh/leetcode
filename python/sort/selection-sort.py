#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/5
"""


class SelectionSort(object):
    def selection_sort(self, nums):
        if len(nums) <= 1:
            return nums

        for i in range(len(nums)-1):
            min_index = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j

            if min_index != i:
                nums[min_index], nums[i] = nums[i], nums[min_index]

        return nums

if __name__ == "__main__":
    import random
    l = [random.randint(0, 100) for _ in range(10)]
    print(SelectionSort().selection_sort(l))
