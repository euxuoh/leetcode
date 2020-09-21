#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
49. Group Anagrams
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/29
"""
from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group = defaultdict(list)

        for s in strs:
            group[''.join(sorted(s))].append(s)

        return [v for _, v in group.items()]


if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
