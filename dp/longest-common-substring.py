#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
longest common substring

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/13
"""


class Solution(object):
    def LCSstr_dp(self, s, t):
        """
        :param s:
        :param t:
        :return:
        """
        def lcs_len(s, t):
            """
            dp[i][j] = dp[i-1][j-1] + 1, if s[i]==t[j];
            dp[i][j] = 0, if s[i]!=t[j]
            :param s:
            :param t:
            :return:
            """
            m, n = len(s), len(t)
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            max_len, max_index = 0, 0
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if s[i - 1] == t[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                        if dp[i][j] > max_len:
                            max_len = dp[i][j]
                            max_index = i - max_len
            # print(dp)
            # print(max_index, max_len)
            return max_index, max_len

        index, l = lcs_len(s, t)
        return s[index: index+l]

    def LCSs_suffix(self, s, t):
        """
        :param s:
        :param t:
        :return:
        """
        def common_length(s1, s2):
            length = 0
            for ch in zip(s1, s2):
                if ch[0] == ch[1]:
                    length += 1
                else:
                    break
            return length

        new_str = s + '#' + t
        suffix = [new_str[i:] for i in range(len(new_str))]
        suffix.sort()
        _max_length = 0

        for i in range(len(suffix)-2):
            _max_length = max(_max_length, common_length(suffix[i], suffix[i+1]))

        return _max_length

if __name__ == "__main__":
    print(Solution().LCSstr_dp('acaccbabb', 'acbac'))
    print(Solution().LCSs_suffix('acaccbabb', 'acbac'))
