#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
347. Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/28
"""
from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        """hash + heap
        Time: O(n * log(K)), because most_common()的实现用了堆模块heapq
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return zip(*Counter(nums).most_common(k))[0]
        # return [num for num, f in Counter(nums).most_common(k)]

    def top_k_freq(self, nums, k):
        """
        Time: O(n)
        :param nums:
        :param k:
        :return:
        """
        cnt = Counter(nums)
        freq_list = [[] for i in range(len(nums)+1)]
        for num, f in cnt.items():
            freq_list[f].append(num)
        ans = []
        for freq in freq_list[::-1]:
            ans += freq
        return ans[:k]


if __name__ == "__main__":
    solution = Solution()
    l = [1, 1, 1, 2, 2, 3]
    print(solution.top_k_freq(l, 2))
