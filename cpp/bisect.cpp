#include <bits/stdc++.h>

using namespace std;


int bisect_left(vector<int>& nums, int target) {
    int left = 0, right = nums.size()

    while (left < right) {
        int mid = left + (rigth - left) / 2;
        if (nums[mid] < target){
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    return left;
}

int bisect_right(vector<int>& nums, int target) {
    int left = 0, right = nums.size();

    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] <= target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    return left;
}