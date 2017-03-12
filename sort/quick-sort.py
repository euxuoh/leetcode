#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc string

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/5
"""


class QuickSort(object):
    def quick_sort(self, nums):
        if len(nums) <= 1:
            return nums

        return self.quick_sort([x for x in nums[1:] if x <= nums[0]]) + [nums[0]] + \
            self.quick_sort([x for x in nums[1:] if x > nums[0]])

    def partition(self, nums, low, high):
        privot = nums[low]

        while low < high:
            while low < high and nums[high] >= privot:
                high -= 1
            nums[low], nums[high] = nums[high], nums[low]

            while low < high and nums[low] <= privot:
                low += 1
            nums[low], nums[high] = nums[high], nums[low]
        print(nums, privot)
        return low

    def quick_sort_recursion(self, nums, low, high):
        if low < high:
            privot = self.partition(nums, low, high)
            self.quick_sort_recursion(nums, low, privot-1)
            self.quick_sort_recursion(nums, privot+1, high)

    def quick_sort_iteration(self, nums, low, high):
        stack = []

        if low < high:
            privot = self.partition(nums, low, high)
            if privot - 1 > low:
                stack.append(low)
                stack.append(privot-1)
            if privot + 1 < high:
                stack.append(privot+1)
                stack.append(high)

            while stack:
                print(stack)
                right = stack.pop()
                left = stack.pop()
                p = self.partition(nums, left, right)
                if p - 1 > left:
                    stack.append(left)
                    stack.append(p-1)
                if p + 1 < right:
                    stack.append(p+1)
                    stack.append(right)

if __name__ == "__main__":
    import random

    l = [random.randint(0, 100) for _ in range(10)]
    # print(QuickSort().quick_sort(l))

    # QuickSort().quick_sort_recursion(l, 0, len(l)-1)
    # print(l)

    QuickSort().quick_sort_iteration(l, 0, len(l)-1)
    print(l)
