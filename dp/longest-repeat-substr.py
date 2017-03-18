#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
最长重复子串

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/12
"""


class Solution(object):
    def lrs_basic(self, s):
        """最基本的解法
        :param s:
        :return:
        """
        pass

    def lrs_suffix(self, s):
        """后缀数组

        :param s:
        :return:
        """
        suffix = [s[i:] for i in range(len(s))]
        suffix.sort()
        _max_length = 0
        for i in range(len(suffix)-2):
            length = self.common_length(suffix[i], suffix[i+1])
            _max_length = max(_max_length, length)
        return _max_length

    def common_length(self, s1, s2):
        length = 0
        for ch in zip(s1, s2):
            if ch[0] == ch[1]:
                length += 1
            else:
                break
        return length


if __name__ == "__main__":
    print(Solution().lrs_suffix('banana'))
