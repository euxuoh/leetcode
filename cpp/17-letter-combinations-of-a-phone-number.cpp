#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.size() == 0) {
            return {};
        }

        string path;

        dfs(digits, 0, path);

        return res;
    }

    void dfs(string& digits, int index, string& path) {
        if (path.size() == digits.size()) {
            res.push_back(path);
            return;
        }

        for (int i = 0; i < pairs[digits[index]].size(); ++i) {
            path.push_back(pairs[digits[index]][i]);
            dfs(digits, index+1, path);
            path.pop_back();
        }
    }
    
private:
    vector<string> res;
    unordered_map<char, string> pairs = {
        {'2', "abc"}, {'3', "def"}, {'4', "ghi"}, 
        {'5', "jkl"}, {'6', "mno"}, {'7', "pqrs"}, 
        {'8', "tuv"}, {'9', "wxyz"}
    };
};