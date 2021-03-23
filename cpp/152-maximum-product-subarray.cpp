#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int min_end = 1, max_end = 1, res = INT_MIN;

        for (int num : nums) {
            if (num < 0) {
                swap(max_end, min_end);
            }

            max_end = max(max_end * num, num);
            min_end = min(min_end * num, num);

            res = max(max_end, res);
        }

        return res;
    }

    int maxProduct2(vector<int>& nums) {
        if (nums.empty()) return 0;

        int max_end, min_end, res;
        max_end = min_end = res = nums[0];

        for (int i = 1; i < nums.size(); ++i) {
            int end1 = max_end * nums[i];
            int end2 = min_end * nums[i];
            max_end = max(max(end1, end2), nums[i]);
            min_end = min(min(end1, end2), nums[i]);
            res = max(res, max_end);
        }

        return res;
    }
};
