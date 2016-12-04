#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
80. Remove Duplicates from Sorted Array II

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
It doesn't matter what you leave beyond the new length.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/1
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        last, i, same = 0, 1, False
        while i < len(nums):
            if nums[last] != nums[i] or not same:
                same = nums[last] == nums[i]
                last += 1
                nums[last] = nums[i]
            i += 1

        return last + 1

if __name__ == "__main__":
    solution = Solution()
    test1 = [1, 1, 1, 2, 2, 3, 3]
    print solution.removeDuplicates(test1)
    print test1
