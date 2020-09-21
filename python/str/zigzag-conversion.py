#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern
on a given number of rows like this: (you may want to display
this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this
conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/1/9
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        ans = ''
        step = 2 * numRows - 2
        for i in range(numRows):
            for j in range(i, len(s), step):
                ans += s[j]
                if 0 < i < numRows - 1 and j + step - 2 * i < len(s):
                    ans += s[j + step - 2 * i]

        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.convert("abcde", 4))
