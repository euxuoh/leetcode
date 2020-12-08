#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    int longestPalindromeSubseq(string s) {
        // dp[i][j]定义为s(i...j)的最长回文子序列长度
        // dp[i][j] = 0, i > j
        //          = 1, i = j
        //          = max(dp[i+1][j], dp[i][j-1]), i < j && s[i] != s[j]
        //          = dp[i+1][j-1] + 2, i < j && s[i] == s[j]
        int n = s.size();

        vector<vector<int>> dp(n, vector<int>(n, 0));

        for (int i = 0; i < n; ++i) {
            dp[i][i] = 1;
        }

        for (int i = n-2; i >= 0; --i) {
            for (int j = i+1; j < n; ++j) {
                if (s[i] == s[j]) {
                    dp[i][j] = dp[i+1][j-1] + 2;
                } else {
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1]);
                }
            }
        }

        return dp[0][n-1];
    }
};