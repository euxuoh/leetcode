#include <bits/stdc++.h>

using namespace std;


int longestSubstrWithoutRepeat(string str) {
    if (str.empty()) {
        return 0;
    }

    unordered_set<char> lookup;
    int left = 0, max_len = 1;

    for (int i = 0; i < str.size(); ++i) {
        while (lookup.count(str[i])) {
            lookup.erase(str[left]);
            left++;
        }

        max_len = max(max_len, i-left+1);
        lookup.insert(str[i]);
    }

    return max_len;
}
