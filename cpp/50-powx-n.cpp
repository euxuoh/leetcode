#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    double myPow(double x, long long n) {
        if (x == 1.0 || n == 0) {
            return 1.0;
        }

        if (n < 0) {
            return 1 / myPow(x, -n);
        }

        if (n % 2 == 1) {
            return x * myPow(x, n-1);
        }

        return myPow(x*x, n/2);
    }
};
