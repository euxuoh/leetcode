#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
29. Divide Two Integers

Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/9
"""


class Solution(object):
    def divide(self, dividend, divisor):
        """
        Time limit exceed
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        result, dvd, dvs = 0, abs(dividend), abs(divisor)

        while dvd >= dvs:
            dvd -= dvs
            result += 1

        if divisor < 0 < dividend or dividend < 0 < divisor:
            return -result
        else:
            return result

    def divide2(self, dividend, divisor):
        """
        :param dividend: int
        :param divisor: int
        :return: int
        """
        result, dvd, dvs = 0, abs(dividend), abs(divisor)

        while dvd >= dvs:
            ins = dvs
            i = 1
            while dvd >= ins:
                dvd -= ins
                result += i
                i <<= 1
                ins <<= 1

        if divisor < 0 < dividend or dividend < 0 < divisor:
            return -result
        else:
            return result


if __name__ == "__main__":
    print(Solution().divide(123, 12))
    print(Solution().divide(-123, 12))
    print(Solution().divide(123, -12))
    print(Solution().divide(-123, -12))
