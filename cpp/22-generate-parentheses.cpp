#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;

        generate(res, n, 0, 0, "");

        return res;
    }

    void generate(vector<string>& res, int n, int left, int right, string path) {
        if (left == n && right == n) {
            res.push_back(path);
            return;
        }

        if (left < n) {
            generate(res, n, left+1, right, path+"(");
        }

        if (right < n && right < left) {
            generate(res, n, left, right+1, path+")");
        }
    }
};
