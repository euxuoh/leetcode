#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/5
"""
import math


class RadixSort(object):
    def radix_sort(self, nums, radix=10):
        if len(nums) <= 1:
            return nums

        k = math.ceil(math.log(max(nums), radix)) + 1
        buckets = [[] for _ in range(radix)]
        for i in range(1, k+1):
            for num in nums:
                buckets[num % (radix**i)//(radix**(i-1))].append(num)
            del nums[:]
            for bucket in buckets:
                nums.extend(bucket)

            buckets = [[] for _ in range(radix)]

        return nums

if __name__ == "__main__":
    import random

    l = [random.randint(0, 100) for _ in range(10)]
    l.append(100)
    print(RadixSort().radix_sort(l))

