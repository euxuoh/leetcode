#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
剑指offer
面试题三：二维数组中的查找

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/4/8
"""


def search_sorted_matrix(matrix, target):
    """从矩阵的右上角开始查找，如果找到返回行列索引；
    如果当前元素比目标大，左移，列索引减一；
    如果当前元素比目标小，下移，行索引加一；
    如果没找到，返回(-1, -1)

    :param matrix: List[List[]]
    :param target: Int
    :return: Tuple(row_index, col_index)
    """
    rows = len(matrix)
    if rows == 0:
        return -1, -1
    cols = len(matrix[0])
    if cols == 0:
        return -1, -1

    row, col = 0, cols-1
    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return row, col
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    return -1, -1

if __name__ == "__main__":
    m1 = []
    m2 = [[], [], []]
    m3 = [[1, 5, 9], [2, 6, 10], [3, 7, 11]]
    assert search_sorted_matrix(m1, 1) == (-1, -1)
    assert search_sorted_matrix(m2, 1) == (-1, -1)
    assert search_sorted_matrix(m3, 1) == (0, 0)
    assert search_sorted_matrix(m3, 9) == (0, 2)
    assert search_sorted_matrix(m3, 3) == (2, 0)
    assert search_sorted_matrix(m3, 4) == (-1, -1)
