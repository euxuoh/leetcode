#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
350. Intersection of Two Arrays II
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that
    you cannot load all elements into the memory at once?

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/11/26
"""
from collections import defaultdict


def binary_search(nums, left, right, target):
    while left < right:
        mid = left + (right - left) / 2

        if target <= nums[mid]:
            right = mid
        else:
            left = mid + 1

    return left


class Solution(object):
    def intersect(self, nums1, nums2):
        """数组没有排序，且没有内存限制
            Time: O(m+n)
            Space: O(min(m, n))

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        nums1_dict = defaultdict(int)
        for num in nums1:
            nums1_dict[num] += 1

        res = []
        for num in nums2:
            if nums1_dict[num] > 0:
                res.append(num)
                nums1_dict[num] -= 1

        return res

    def sorted_intersect(self, nums1, nums2):
        """输入的数组有序，内存受限
            Time: O(min(m, n) * log(max(m, n)))
            Space: O(1)
        :param nums1: List[int]
        :param nums2: List[int]
        :return: List[int]
        """
        if len(nums1) > len(nums2):
            return self.sorted_intersect(nums2, nums1)

        nums1.sort()
        nums2.sort()  # 确认数据有序，不计入时间复杂度

        res = []
        left = 0
        for num in nums1:
            left = binary_search(nums2, left, len(nums2), num)
            if left != len(nums2) and nums2[left] == num:
                res.append(num)
                left += 1

        return res

    def unsorted_intersect(self, nums1, nums2):
        """输入的数组无序，内存受限
            Time: O(max(m, n) * log(max(m, n)))
            Space: O(1)
        :param nums1: List[int]
        :param nums2: List[int]
        :return: List[int]
        """
        nums1.sort(), nums2.sort()

        res = []
        iter1, iter2 = 0, 0

        while iter1 < len(nums1) and iter2 < len(nums2):
            if nums1[iter1] < nums2[iter2]:
                iter1 += 1
            elif nums1[iter1] > nums2[iter2]:
                iter2 += 1
            else:
                res.append(nums1[iter1])
                iter1 += 1
                iter2 += 1

        return res


if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    # assert solution.intersect(nums1, nums2) == [2, 2]
    # assert solution.unsorted_intersect(nums1, nums2) == [2, 2]
    assert solution.sorted_intersect(nums1, nums2) == [2, 2]
