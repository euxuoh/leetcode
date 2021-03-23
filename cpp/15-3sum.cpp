#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        if (nums.size() <= 2) {
            return ans;
        }

        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size()-2; ++i) {
            if (nums[i] > 0) {
                break;
            }
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }

            int low = i + 1, high = nums.size() - 1;
            while (low < high) {
                int sum = nums[i] + nums[low] + nums[high];
                if (sum < 0) {
                    while (low < high && nums[low] == nums[++low]);
                } else if (sum > 0) {
                    while (low < high && nums[high] == nums[--high]);
                } else {
                    ans.push_back({nums[i], nums[low], nums[high]});
                    while (low < high && nums[low] == nums[++low]);
                    while (low < high && nums[high] == nums[--high]);
                }
            }
        }

        return ans;
    }
};
