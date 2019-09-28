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
        pivot = nums[low]

        while low < high:
            while low < high and nums[high] >= pivot:
                high -= 1
            nums[low], nums[high] = nums[high], nums[low]

            while low < high and nums[low] <= pivot:
                low += 1
            nums[low], nums[high] = nums[high], nums[low]

        return low

    def quick_sort_recursion(self, nums, low, high):
        if low < high:
            pivot = self.partition(nums, low, high)
            self.quick_sort_recursion(nums, low, pivot-1)
            self.quick_sort_recursion(nums, pivot+1, high)

    def quick_sort_iteration(self, nums, low, high):
        stack = []

        if low < high:
            pivot = self.partition(nums, low, high)
            if pivot - 1 > low:
                stack.append(low)
                stack.append(pivot-1)
            if pivot + 1 < high:
                stack.append(pivot+1)
                stack.append(high)

            while stack:
                print(stack)
                high = stack.pop()
                low = stack.pop()
                pivot = self.partition(nums, low, high)
                if pivot - 1 > low:
                    stack.append(low)
                    stack.append(pivot-1)
                if pivot + 1 < high:
                    stack.append(pivot+1)
                    stack.append(high)


if __name__ == "__main__":
    import random

    l = [random.randint(0, 100) for _ in range(10)]
    # print(QuickSort().quick_sort(l))

    # QuickSort().quick_sort_recursion(l, 0, len(l)-1)
    # print(l)

    QuickSort().quick_sort_iteration(l, 0, len(l)-1)
    print(l)
