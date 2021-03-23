#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        queue<string> q({beginWord});

        int step = 1;
        while (!q.empty()) {
            int n = q.size();
            for (int i = 0; i < n; ++i) {
                string word = q.front();
                q.pop();

                if (word == endWord) {
                    return step;
                }

                for (int j = 0; j < word.size(); ++j) {
                    char c = word[j];
                    for (int k = 'a'; k <= 'z'; ++k) {
                        if (c == k) {
                            continue;
                        }
                        word[j] = k;
                        if (wordSet.count(word)) {
                            q.push(word);
                            wordSet.erase(word);
                        }
                    }
                    word[j] = c;
                }
            }
            step++;
        }

        return 0;
    }
};