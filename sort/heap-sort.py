#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/5
"""


class HeapSort(object):
    def sift_down(self, nums, start, end):
        root = start

        while True:
            child = 2 * root + 1
            if child > end:
                break

            # 始终和较大的子节点互换
            if child + 1 <= end and nums[child] < nums[child+1]:
                child += 1
            if nums[root] < nums[child]:
                nums[root], nums[child] = nums[child], nums[root]
                root = child
            else:
                break

    def heap_sort(self, nums):
        # 创建最大堆
        for start in range((len(nums)-2)//2, -1, -1):
            self.sift_down(nums, start, len(nums)-1)

        for end in range(len(nums)-1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            self.sift_down(nums, 0, end-1)

        return nums


if __name__ == "__main__":
    import random

    l = [random.randint(0, 99) for _ in range(10)]
    print(HeapSort().heap_sort(l))
