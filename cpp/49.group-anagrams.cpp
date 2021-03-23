#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // 特例
        if (strs.empty()) return {};
        if (strs.size() == 1) return {strs};

        vector<vector<string>> res;
        unordered_map<string, int> str_index;
        int index = 0;

        for (string str : strs) {
            string tmp = str;
            sort(tmp.begin(), tmp.end());

            if (str_index.count(tmp)) {
                // 已存在
                res[str_index[tmp]].push_back(str);
            } else {
                // 首次出现
                res.push_back({str});
                str_index[tmp] = index;
                index++;
            }
        }

        return res;
    }
};
