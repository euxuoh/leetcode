#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/5
"""


class MergeSort(object):
    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums

        def merge(l, r):
            merged = []

            while l and r:
                merged.append(l.pop(0) if l[0] < r[0] else r.pop(0))
            merged.extend(l if l else r)

            return merged

        mid_index = len(nums) // 2
        left = self.merge_sort(nums[:mid_index])
        right = self.merge_sort(nums[mid_index:])

        return merge(left, right)


if __name__ == "__main__":
    import random

    l = [random.randint(0, 100) for _ in range(10)]
    print(MergeSort().merge_sort(l))
