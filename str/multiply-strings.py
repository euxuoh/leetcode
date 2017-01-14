#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/1/9
"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return 0

        if len(num1) < len(num2):
            return self.multiply(num2, num1)
        ans = ''
        for i in range(len(num2)):
            product = self.single_multiply(num1, num2[-(i+1)]) + '0' * i
            ans = self.add(ans, product)

        return ans

    def add(self, num1, num2):
        result, carry, val = '', 0, 0
        for i in range(max(len(num1), len(num2))):
            val = carry
            if i < len(num1):
                val += int(num1[-(i+1)])
            if i < len(num2):
                val += int(num2[-(i+1)])
            carry, val = val // 10, val % 10
            result += str(val)

        if carry:
            result += str(carry)

        return result[::-1]

    def single_multiply(self, num, n):
        result, carry, val = '', 0, 0

        for i in range(len(num)):
            val = carry
            val += int(n) * int(num[-(i+1)])
            carry, val = val // 10, val % 10
            result += str(val)

        if carry:
            result += str(carry)

        return result[::-1]


if __name__ == "__main__":
    solution = Solution()
    # print(solution.single_multiply('1000000000000000000000000000', '8'))
    # print(solution.add('1230', '32100000'))
    print(solution.multiply('99999999999999999999', '1000000000000000000000000000'))
