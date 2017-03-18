#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
long palindrome substring

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/13
"""


class Solution(object):
    def LPS_basic(self, s):
        """
        枚举中心位置，然后再在该位置上用扩展法，记录并更新得到的最长的回文长度
        :param s:
        :return:
        """
        if len(s) < 1:
            return 0
        i, max_len = 0, 0
        c = 0
        for i in range(len(s)):
            # 以i为中心，长度为偶数
            j = 0
            while i - j >= 0 and i + j < len(s):
                if s[i - j] != s[i + j]:
                    break
                c = 2 * j + 1
                j += 1
            max_len = max(max_len, c)
            # 以i为中心，长度为奇数
            j = 0
            while i - j >= 0 and i + j + 1 < len(s):
                if s[i - j] != s[i + j + 1]:
                    break
                c = 2 * j + 2
                j += 1
            max_len = max(max_len, c)
        return max_len

    def manacher(self, s):
        """manacher算法
        step 1: 令RL[i]=min(RL[2*pos-i], MaxRight-i)
        step 2: 以i为中心扩展回文串，直到左右两边字符不同，或者到达边界。
        step 3: 更新MaxRight和pos
        reference：https://segmentfault.com/a/1190000003914228
        :param s:
        :return:
        """
        s = '#' + '#'.join(s) + '#'
        max_right, pos, max_len = 0, 0, 0
        p = [0] * len(s)

        for i in range(len(s)):
            if i < max_right:
                p[i] = min(p[2*pos-i], max_right-i)
            else:
                p[i] = 1

            while i - p[i] >= 0 and i + p[i] < len(s) and s[i-p[i]] == s[i+p[i]]:
                p[i] += 1

            if i + p[i] + 1 > max_right:
                max_right = i + p[i] + 1
                pos = i

            max_len = max(max_len, p[i])

        return max_len - 1


if __name__ == "__main__":
    print(Solution().manacher('aaaaaa'))
