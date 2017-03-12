#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/5
"""


class CountSort(object):
    def count_sort(self, nums):
        if len(nums) <= 1:
            return nums

        _min, _max = min(nums), max(nums)
        count, res = [0] * (_max-_min+1), [0] * len(nums)

        for n in nums:
            count[n-_min] += 1

        for i in range(1, len(count)):
            count[i] += count[i-1]

        for i in range(len(nums)-1, -1, -1):
            res[count[nums[i]-_min]-1] = nums[i]

        return res


if __name__ == "__main__":
    import random

    l = [random.randint(0, 100) for _ in range(10)]
    print(CountSort().count_sort(l))

