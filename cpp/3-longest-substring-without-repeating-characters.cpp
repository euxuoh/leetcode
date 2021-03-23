#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.empty()) {
            return 0;
        }

        unordered_set<char> lookup;
        int left = 0, max_len = 1;

        for (int i = 0; i < s.size(); ++i) {
            while (lookup.count(s[i])) {
                lookup.erase(s[left]);
                left++;
            }
            max_len = max(max_len, i-left+1);
            lookup.insert(s[i]);
        }

        return max_len;
    }
};
