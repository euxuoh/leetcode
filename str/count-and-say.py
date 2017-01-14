#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
38. Count and Say

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/1/9
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = '1'
        for i in range(n-1):
            ans = self.trans(ans)
        return ans

    def trans(self, num):
        i, result = 0, ''

        while i < len(num):
            cnt = 1
            while i < len(num)-1 and num[i] == num[i+1]:
                cnt += 1
                i += 1
            result += str(cnt) + num[i]
            i += 1

        return result


if __name__ == "__main__":
    solution = Solution()
    for i in range(10):
        print(solution.countAndSay(i))
