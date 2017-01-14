#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
468. Validate IP Address

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/1/12
"""
import string


class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        blocks = IP.split('.')
        if len(blocks) == 4:
            for block in blocks:
                if not block.isdigit() or not 0 <= int(block) < 256 \
                        or (block[0] == '0' and len(block) > 1):
                    return "Neither"
            return "IPv4"

        blocks = IP.split(':')
        if len(blocks) == 8:
            for block in blocks:
                if not (1 <= len(block) <= 4) or not all(c in string.hexdigits for c in block):
                    return "Neither"
            return "IPv6"

        return "Neither"

if __name__ == "__main__":
    solution = Solution()
    print(solution.validIPAddress("172.16.04.1"))
    print(solution.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
    print(solution.validIPAddress("256.256.256.256"))
    print(solution.validIPAddress("1.0.1."))
