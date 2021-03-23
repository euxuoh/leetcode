#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        if (nums.empty()) return {{}};

        vector<int> path;

        backtracking(nums, 0, path);

        return res;
    }

    void backtracking(vector<int>& nums, int index, vector<int>& path) {
        res.push_back(path);

        for (int i = index; i < nums.size(); ++i) {
            path.push_back(nums[i]);

            backtracking(nums, i+1, path);

            path.pop_back();
        }
    }

private:
    vector<vector<int>> res;
};
