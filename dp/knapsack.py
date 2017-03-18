#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
背包问题

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/17
"""


class Knapsack(object):
    def zero_one_knapsack(self, val, wt, W):
        """
        dp[i][j]表示前i个物品装到剩余体积为j的背包里能达到的最大价值
        如果不放入第i个物品, 则价值为前i-1个商品放入剩余体积为j的背包的最大价值
            dp[i][j] = dp[i-1][j]
        如果放入第i个物品, 则价值为前i-1个商品放入剩余体积为j-wt[i]的背包达到的最大价值,
        加上第i个物品的价值, 所以状态转移方程为
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-wt[i]]+val[i])

        :param val: List[int] 每个物品的价值
        :param wt: List[int] 每个物品的重量
        :param W: int 背包容纳的总重量
        :return result: int 最大价值
        """
        num_of_goods = len(val)
        val_matrix = [[0] * (W+1) for _ in range(num_of_goods+1)]

        for i in range(1, num_of_goods+1):
            for j in range(1, W+1):
                if wt[i-1] <= j:  # 可以放入
                    val_matrix[i][j] = max(val_matrix[i-1][j], val_matrix[i-1][j-wt[i-1]]+val[i-1])
                else:
                    val_matrix[i][j] = val_matrix[i-1][j]

        return val_matrix[-1][-1]

if __name__ == "__main__":
    print(Knapsack().zero_one_knapsack([10, 40, 30, 50], [5, 4, 6, 3], 10))
