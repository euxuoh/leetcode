#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
longest common sub-sequence

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/12
"""


class Solution(object):
    def lcs_basic(self, s, t):
        """

        :param s: string
        :param t: string
        :return:
        """
        pass

    def lcs_dp(self, s, t):
        """
        设序列 X=<x1, x2, …, xm> 和 Y=<y1, y2, …, yn> 的一个最长公共子序列 Z=<z1, z2, …, zk>，则:
        1.若 xm = yn，则 zk = xm = yn 则 Zk-1 是 Xm-1 和 Yn-1 的最长公共子序列;
        2.若 xm ≠ yn， 要么Z是 Xm-1 和 Y 的最长公共子序列，要么 Z 是X和 Yn-1 的最长公共子序列。
            2.1 若 xm ≠ yn 且 zk≠xm ，则 Z是 Xm-1 和 Y 的最长公共子序列；
            2.2 若 xm ≠ yn 且 zk ≠yn ，则 Z 是X和 Yn-1 的最长公共子序列。
        综合一下2 就是求二者的大者
        :param s: string
        :param t: string
        :return:
        """
        dp = self.lcs_length(s, t)
        self.lcs_print(dp, s, t, len(s), len(t))

    def lcs_length(self, s, t):
        """
        构造二维数组dp[i][j], 记录s[i]和t[j]的LCS长度, (i, j)是前缀
        dp[i][j] = 0, if i == j == 0
        dp[i][j] = dp[i-1][j-1] + 1, if i, j > 0 and s[i] == t[j]
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]), if i, j > 0 and s[i] != t[j]
        :param s:
        :param t:
        :return:
        """
        m, n = len(s), len(t)

        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp

    def lcs_print(self, dp, s, t, m, n):
        if m == 0 or n == 0:
            return

        if s[m-1] == t[n-1]:
            print(s[m-1])
            self.lcs_print(dp, s, t, m-1, n-1)
        elif dp[m-1][n] >= dp[m][n-1]:
            self.lcs_print(dp, s, t, m-1, n)
        else:
            self.lcs_print(dp, s, t, m, n-1)


if __name__ == "__main__":
    Solution().lcs_dp('abcbdab', 'bdcaba')
