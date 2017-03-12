#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
287. Find the Duplicate Number

Given an array nums containing n + 1 integers where each integer
is between 1 and n (inclusive), prove that at least one duplicate
number must exist. Assume that there is only one duplicate number,
find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be
repeated more than once.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/9
"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 1, len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            cnt = sum(num <= mid for num in nums)
            if cnt > mid:
                right = mid - 1
            else:
                left = mid + 1

        return left

    def findDuplicate2(self, nums):
        """
        看做有环链表
        :param nums:
        :return: int
        """
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

if __name__ == "__main__":
    pass
