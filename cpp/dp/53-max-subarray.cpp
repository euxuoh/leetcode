#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int cur_sum = 0, max_sum = nums[0];

        for (int num : nums) {
            if (cur_sum > 0) {
                cur_sum += num;
            } else {
                cur_sum = num;
            }
            max_sum = max(max_sum, cur_sum);
        }

        return max_sum;
    }
};

int maxSubArray(vector<int> &nums) {
    if (nums.empty()) return 0;
    
    int cur_sum = 0, max_sum = nums[0];

    for (int num : nums) {
        cur_sum = max(cur_sum, num);
        max_sum = max(max_sum, cur_sum);
    }

    return max_sum;
}

int main() {
    vector<int> nums = {1, 2, 4, 7, 2, 1, 1, 0};

    int res = maxSubArray(nums);

    return 0;
}
