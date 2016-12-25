#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
187. Repeated DNA Sequences

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/29
"""


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        from collections import defaultdict
        res = []
        seq_dict = defaultdict(int)
        for i in range(len(s)-10+1):
            seq_dict[s[i:i+10]] += 1

        print(seq_dict)

        for k, v in seq_dict.items():
            if v > 1:
                res.append(k)

        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
    print(solution.findRepeatedDnaSequences("AAAAAAAAAAA"))
