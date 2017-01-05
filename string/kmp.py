#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
KMP 算法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/1/4
"""


class KMP(object):
    def brute_force(self, s, p):
        s_len, p_len = len(s), len(p)
        i, j = 0, 0

        while i < s_len and j < p_len:
            if s[i] == p[j]:
                i += 1
                j += 1
            else:
                i = i - j + 1
                j = 0

        if j == p_len:
            return i - j
        else:
            return -1

    def kmp(self, s, p):
        s_len, p_len = len(s), len(p)
        _next = self.get_next(p)
        i, j = 0, 0

        while i < s_len and j < p_len:
            if s[i] == p[j]:
                i, j = i + 1, j + 1
            else:
                j = _next[j]

        if j == p_len:
            return i - j
        else:
            return -1

    def get_max_length(self, p):
        size = len(p)
        _next = [0] * size

        for i in range(1, size):
            k = _next[i-1]
            while p[i] != p[k] and k:
                k = _next[k-1]
            if p[i] == p[k]:
                _next[i] = k + 1

        return _next

    def get_next(self, p):
        _next = [-1]
        k, j = -1, 0

        while j < len(p) - 1:
            if k == -1 or p[k] == p[j]:
                k, j = k + 1, j + 1
                _next.append(k)
            else:
                k = _next[k]

        return _next

    def get_next_better(self, p):
        _next = [-1]
        k, j = -1, 0

        while j < len(p) - 1:
            if k == -1 or p[k] == p[j]:
                k, j = k + 1, j + 1
                if p[k] == p[j]:
                    _next.append(k)
                else:
                    _next.append(_next[k])
            else:
                k = _next[k]

        return _next


if __name__ == "__main__":
    solution = KMP()
    print(solution.brute_force('abca', 'bca'))
    print(solution.get_next('ababababab'))
    print(solution.get_next_better('ababababab'))
