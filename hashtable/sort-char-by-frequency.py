#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
451. Sort Characters By Frequency


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/28
"""
from collections import Counter


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        freq = Counter(s)
        order_freq = sorted(zip(freq.values(), freq.keys()), reverse=True)
        for f, c in order_freq:
            ans += c * f
        return ans

    def frequency_sort(self, s):
        """pythonic
        :param s:
        :return:
        """
        return ''.join(sorted(Counter(s).elements()))
        # return ''.join(c * f for c, f in Counter(s).most_common())


if __name__ == "__main__":
    solution = Solution()
    print(solution.frequencySort('aaab'))
    print(solution.frequencySort('aAbb'))
