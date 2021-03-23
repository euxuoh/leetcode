#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        if (n < 2) {
            return s;
        }

        // dp[i,j]: s[i...j]是否是回文串
        vector<vector<bool>> dp(n, vector<bool>(n, false));

        for (int i = 0; i < n; ++i) {
            dp[i][i] = true;
        }

        int begin = 0, max_len = 1;
        for (int i = n-2; i >= 0; --i) {
            for (int j = i+1; j < n; ++j) {
                if (s[i] == s[j]) {
                    if (j-i < 3) {
                        dp[i][j] = true;
                    } else {
                        dp[i][j] = dp[i+1][j-1];
                    }
                } else {
                    dp[i][j] = false;
                }

                if (dp[i][j]) {
                    int cur_len = j-i+1;
                    if (cur_len > max_len) {
                        max_len= cur_len;
                        begin = i;
                    }
                }
            }
        }

        return s.substr(begin, max_len);
    }
};