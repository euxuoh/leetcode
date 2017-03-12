#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
179. Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/6
"""


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        from functools import cmp_to_key
        key = cmp_to_key(lambda x, y: int(y+x) - int(x+y))
        return ''.join(sorted(map(str, nums), key=key)).lstrip('0') or '0'

if __name__ == "__main__":
    print(Solution().largestNumber([3, 30, 34, 5, 9]))
