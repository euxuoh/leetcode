#include <bits/stdc++.h>

using namespace std;


int partition(vector<int>& nums, int left, int right) {
    int pivot = nums[left];

    while (left < right) {
        while (left < right && nums[right] >= pivot) {
            --right;
        }
        swap(nums[left], nums[right]);
        while (left < right && nums[left] <= pivot) {
            ++left;
        }
        swap(nums[left], nums[right]);
    }

    return left;
}

int find_kth_largest(vector<int>& nums, int k) {
    if (nums.size() < k) {
        return -1;
    }

    k = nums.size() - k;
    int left = 0, right = nums.size()-1;

    while (left <= right) {
        int index = partition(nums, left, right);
        if (index == k) {
            return nums[k];
        } else if (index < k) {
            left = index + 1;
        } else {
            right = index - 1;
        }
    }

    return -1;
}

int main() {
    vector<int> nums = {3,2,1,5,6,4};

    cout << find_kth_largest(nums, 6) << endl;
    cout << find_kth_largest(nums, 5) << endl;
    cout << find_kth_largest(nums, 4) << endl;
    cout << find_kth_largest(nums, 3) << endl;
    cout << find_kth_largest(nums, 1) << endl;

    return 0;
}
