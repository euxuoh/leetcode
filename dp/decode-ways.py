#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
91. Decode Ways

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/17
"""


class Solution(object):
    def decode_ways(self, s):
        """

        :param s:
        :return:
        """
        length = len(s)
        if length == 0 or s[0] == '0':
            return 0

        dp = [0] * (length + 1)
        dp[length] = 1
        dp[length-1] = 1 if s[-1] != '0' else 0

        for i in range(length-2, -1, -1):
            if s[i] == '0':
                continue
            else:
                if int(s[i:i+2]) <= 26:
                    dp[i] = dp[i+1] + dp[i+2]
                else:
                    dp[i] = dp[i+1]

        return dp[0]

if __name__ == "__main__":
    print(Solution().decode_ways('010323'))
