#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
剑指offer
面试题四：替换空格

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/4/8
"""


def replace_blank(string):
    """

    :param string: List[char]
    :return:
    """
    if not string:
        return

    num_of_blank, size = 0, len(string)
    for ch in string:
        if ch == ' ':
            num_of_blank += 1

    string += [''] * num_of_blank * 2

if __name__ == "__main__":
    pass
