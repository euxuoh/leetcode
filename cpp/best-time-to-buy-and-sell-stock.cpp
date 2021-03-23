#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    // 121. 只能交易一次
    int maxProfit1(vector<int>& prices) {
        int profit = 0, min_price = 1e9;
        for (int price : prices) {
            profit = max(profit, price-min_price);
            min_price = min(min_price, price);
        }
        return profit;
    }

    // 122. 可以交易任意次
    int maxProfit2(vector<int>& prices) {
        int profit = 0;
        for (int i = 1; i < prices.size(); ++i) {
            if (prices[i] > prices[i-1]) {
                profit += (prices[i] - prices[i-1]);
            }
        }
        return profit;
    }

    
};