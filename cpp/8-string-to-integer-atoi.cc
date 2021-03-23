#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int strToInt(string str) {
        int i = 0, sign = 1, res = 0;

        while (str[i] == ' ') {
            i++;
        }

        if (str[i] == '-') {
            sign = -1;
        }
        if (str[i] == '-' || str[i] == '+') {
            i++;
        }

        for (; i < str.size() && isdigit(str[i]); i ++) {
            if (res > INT_MAX / 10 || (res == INT_MAX / 10 && str[i] - '0' > 7)) //溢出判定
                return sign == 1 ? INT_MAX : INT_MIN;
            res = res * 10 + (str[i] - '0');
        }

        return sign * res;
    }
};
