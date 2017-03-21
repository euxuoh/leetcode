#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
322. Coin Change

You are given coins of different denominations and a
total amount of money amount. Write a function to compute
the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination
of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/20
"""


class Solution(object):
    def coin_change(self, coins, amount):
        """
        维护一个一维动态数组dp，其中dp[i]表示钱数为i时的最小硬币数，递推式为：
            dp[i+coins[j]] = min{dp[i+coins[j]], dp[i]+1}
        即： dp[i] = min(dp[i], dp[i - coins[j]] + 1);
        其中coins[j]为第j个硬币，而i - coins[j]为钱数i减去其中一个硬币的值，
        剩余的钱数在dp数组中找到值，然后加1和当前dp数组中的值做比较，取较小的那个更新dp数组。
        :param coins:
        :param amount:
        :return:
        """
        INF = 0x7fffffff
        dp = [INF] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if coin <= i:  # 可以放入
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[amount] if dp[amount] != INF else -1


if __name__ == "__main__":
    print(Solution().coin_change([1, 2, 5], 11))
