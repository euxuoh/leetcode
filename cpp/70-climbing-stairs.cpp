#include <iostream>

using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        if (n < 3) {
            return n;
        }

        int pre = 1, cur = 2;
        for (int i=3; i<=n; ++i) {
            int next = pre + cur;
            pre = cur;
            cur = next;
        }

        return cur;
    }
};
