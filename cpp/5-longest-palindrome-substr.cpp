#include <bits/stdc++.h>

using namespace std;


string longestPalindromeSubstr(string str) {
    // dp[i, j]表示s[i, j]是否是回文子串
    // basecase dp[i, i] = true, dp[i, j] = false, i > j
    // dp[i, j] = true,            s[i] == s[j] && j-i < 3
    //          = dp[i+1, j-1],    s[i] == s[j]
    //          = false,           s[i] != s[j]

    int n = str.size();
    if (n < 2) {
        return str;
    }

    vector<vector<bool>> dp(n, vector<bool>(n, false));

    for (int i = 0; i < n; ++i) {
        dp[i][i] = true;
    }

    int begin = 0, max_len = 1;
    for (int i = n-2; i >= 0; --i) {
        for (int j = i+1; j < n; ++j) {
            if (str[i-1] == str[j-1]) {
                if (j-i < 3) {
                    dp[i][j] = true;
                } else {
                    dp[i][j] = dp[i+1][j-1];
                }
            } else {
                dp[i][j] = false;
            }

            if (dp[i][j]) {
                int cur_len = j - i + 1;
                if (cur_len > max_len) {
                    max_len = cur_len;
                    begin = i;
                }
            }
        }
    }

    return str.substr(begin, max_len);
}
