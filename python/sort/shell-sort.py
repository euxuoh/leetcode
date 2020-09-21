#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/6
"""


class ShellSort(object):
    def shell_sort(self, nums):
        n = len(nums)
        # 初始步长
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                # 每个步长进行插入排序
                temp = nums[i]
                j = i
                # 插入排序
                while j >= gap and nums[j - gap] > temp:
                    nums[j] = nums[j - gap]
                    j -= gap
                nums[j] = temp
            # 得到新的步长
            gap //= 2
            print(nums)
        return nums


if __name__ == "__main__":
    import random

    l = [random.randint(0, 99) for _ in range(10)]
    print('原始数组：{}'.format(l))
    print(ShellSort().shell_sort(l))
