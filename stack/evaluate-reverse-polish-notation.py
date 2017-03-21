#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
150. Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/20
"""


class Solution(object):
    def evalute_RPN(self, tokens):
        add = lambda a, b: a+b
        sub = lambda a, b: a-b
        mul = lambda a, b: a*b
        div = lambda a, b: a/b+1 if a*b < 0 and a % b != 0 else a/b

        nums, operators = [], {'+': add, '-': sub, '*': mul, '/': div}
        for e in tokens:
            if e not in operators:
                nums.append(int(e))
            else:
                y, x = nums.pop(), nums.pop()
                nums.append(operators[e](x*1.0, y))
        return nums.pop()

if __name__ == "__main__":
    print(Solution().evalute_RPN(["2", "1", "+", "3", "*"]))
    print(Solution().evalute_RPN(["4", "13", "5", "/", "+"]))
    print(Solution().evalute_RPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
    print(Solution().evalute_RPN(["0", "3", "/"]))
