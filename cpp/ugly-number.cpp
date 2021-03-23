#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int nthUglyNumber(int n) {
        if (n < 1) {
            return 0;
        }
        
        vector<int> dp(n);
        dp[0] = 1;

        int p2 = 0, p3 = 0, p5 = 0;

        for (int i = 1; i < n; ++i) {
            int ugly_num = min(min(2*dp[p2], 3*dp[p3]), 5*dp[p5]);
            dp[i] = ugly_num;

            if (ugly_num == 2 * dp[p2]) ++p2;
            if (ugly_num == 3 * dp[p3]) ++p3;
            if (ugly_num == 5 * dp[p5]) ++p5;
        }

        return dp[n-1];
    }
};
