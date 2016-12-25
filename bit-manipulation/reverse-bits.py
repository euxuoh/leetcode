#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
190. Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/15
"""


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            result <<= 1
            result |= n & 1
            n >>= 1
        return result

    def reverse_bit(self, n):
        n = ((n & 0x55555555) << 1) | ((n & 0xAAAAAAAA) >> 1)
        n = ((n & 0x33333333) << 2) | ((n & 0xCCCCCCCC) >> 2)
        n = ((n & 0x0F0F0F0F) << 4) | ((n & 0xF0F0F0F0) >> 4)
        n = ((n & 0x00FF00FF) << 8) | ((n & 0xFF00FF00) >> 8)
        n = ((n & 0x0000FFFF) << 16) | ((n & 0xFFFF0000) >> 16)
        return n


if __name__ == "__main__":
    solution = Solution()
    assert solution.reverseBits(43261596) == 964176192
    assert solution.reverse_bit(43261596) == 964176192
