#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> pair;
        for (int i = 0; i < nums.size(); ++i) {
            if (pair.count(target-nums[i])) {
                return {i, pair[target-nums[i]]};
            }
            pair[nums[i]] = i;
        }
        return {};
    }
};
