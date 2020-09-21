#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
405. Convert a Number to Hexadecimal

Given an integer, write an algorithm to convert it to hexadecimal.
For negative integer, two’s complement method is used.

Note:

1.All letters in hexadecimal (a-f) must be in lowercase.
2.The hexadecimal string must not contain extra leading 0s. If the number is zero,
  it is represented by a single zero character '0';
  otherwise, the first character in the hexadecimal string will not be the zero character.
3.The given number is guaranteed to fit within the range of a 32-bit signed integer.
4.You must not use any method provided by the library which converts/formats the number to hex directly.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/12
"""


class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return '0'

        res = []
        chs = "0123456789abcdef"
        if num < 0:
            num += 0x100000000

        while num:
            res.append(chs[num & 15])
            num >>= 4

        return ''.join(res[::-1])

    def to_hex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return "0"

        result = []
        chs = "0123456789abcdef"
        while num and len(result) != 8:
            result.append(chs[num & 15])
            num >>= 4

        return "".join(result[::-1])


if __name__ == "__main__":
    solution = Solution()
    print(solution.toHex(0))
