#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        if (n < k || k <= 0) {
            return {{}};
        }
        
        vector<vector<int>> res;
        vector<int> path;

        backtracking(res, n, k, 1, path);

        return res;
    }

    void backtracking(vector<vector<int>>& res, int n, int k, int index, vector<int>& path) {
        if (path.size() == k) {
            res.push_back(path);
            return;
        }

        for (int i = index; i <= n; ++i) {
            path.push_back(i);

            backtracking(res, n, k, i+1, path);

            path.pop_back();
        }
    }
};

