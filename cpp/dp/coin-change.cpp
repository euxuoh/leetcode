#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        // dp[i]: 兑换总数为i的至少需要几个硬币
        vector<int> dp(amount+1, amount+1);

        dp[0] = 0;
        for (int i = 1; i <= amount; ++i) {
            for (int coin : coins) {
                if (i >= coin) {
                    dp[i] = min(dp[i], dp[i-coin]+1);
                }
            }
        }

        return dp[amount] == amount+1 ? -1 : dp[amount];
    }

    // 518. 给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个
    int change(int amount, vector<int>& coins) {
        int n = coins.size();

        // dp[i][j]: 只用前i个硬币, 兑换j金额 的组合数
        vector<vector<int>> dp(n+1, vector<int>(amount+1, 0));

        // 兑换0金额, 只有1种方式
        for (int i = 0; i <= n; ++i) {
            dp[i][0] = 1;
        }

        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= amount; ++j) {
                if (j >= coins[i-1]) {
                    // 可以放, 所以是放和不放之和
                    // 1.如果不使用这个coin, 方式同dp[i-1][j]
                    // 2.如果使用这个coin, 方式为dp[i][j-coin]
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]];
                } else {
                    dp[i][j] = dp[i-1][j];
                }
            }
        }

        return dp[n][amount];
    }
};