#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> LIS;

        for (int num : nums) {
            int left = bisect_left(LIS, num);
            if (left == LIS.size()) {
                LIS.push_back(num);
            } else {
                LIS[left] = num;
            }
        }

        return LIS.size();
    }

    int bisect_left(vector<int>& nums, int target) {
        int left = 0, right = nums.size();

        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }
};