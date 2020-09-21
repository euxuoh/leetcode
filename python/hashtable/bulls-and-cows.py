#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
299. Bulls and Cows

You are playing the following Bulls and Cows game with your friend:
You write down a number and ask your friend to guess what the number is.
Each time your friend makes a guess, you provide a hint that indicates
how many digits in said guess match your secret number exactly in both
digit and position (called "bulls") and how many digits match the secret
number but locate in the wrong position (called "cows"). Your friend will
use successive guesses and hints to eventually derive the secret number.

For example:

Secret number:  "1807"
Friend's guess: "7810"
Hint: 1 bull and 3 cows. (The bull is 8, the cows are 0, 1 and 7.)
Write a function to return a hint according to the secret number and friend's guess,
use A to indicate the bulls and B to indicate the cows. In the above example,
your function should return "1A3B".
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2016/12/20
"""
import operator
from collections import Counter


class Solution(object):
    def getHint(self, secret, guess):
        """bull = secret与guess下标与数值均相同的数字个数
        cow = secret与guess中出现数字的公共部分 - bull
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = sum(map(operator.eq, secret, guess))
        cow = sum((Counter(secret) & Counter(guess)).values()) - bull
        return '{}A{}B'.format(bull, cow)


if __name__ == "__main__":
    solution = Solution()
    print(solution.getHint('1807', '7810'))
