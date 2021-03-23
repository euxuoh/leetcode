#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        if (nums.empty()) return {{}};

        sort(nums.begin(), nums.end());

        vector<bool> visited(nums.size(), false);
        vector<int> path;

        backtracking(nums, visited, path);

        return res;
    }

    void backtracking(vector<int>& nums, vector<bool>& visited, vector<int>& path) {
        if (path.size() == nums.size()) {
            res.push_back(path);
            return;
        }

        for (int i = 0; i < nums.size(); ++i) {
            if (visited[i]) {
                continue;
            }

            if (i > 0 && nums[i] == nums[i-1] && !visited[i-1]) {
                continue;
            }

            path.push_back(nums[i]);
            visited[i] = true;

            backtracking(nums, visited, path);

            path.pop_back();
            visited[i] = false;
        }
    }

private:
    vector<vector<int>> res;
};
