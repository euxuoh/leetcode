#include <bits/stdc++.h>

using namespace std;


struct TrieNode {
    unordered_map<char, TrieNode*> children;
    int end;
    TrieNode(): end(0) {}
};

class Trie {
public:
    /** Initialize your data structure here. */
    Trie() {
        root = new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        TrieNode* cur = root;
        for (char ch : word) {
            if (cur->children.count(ch) == 0) {
                cur->children[ch] = new TrieNode();
            }
            cur = cur->children[ch];
        }
        cur->end = 1;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        return find(word, 1);
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        return find(prefix, 0);
    }

    bool find(string word, int exact_match) {
        TrieNode* cur = root;
        for (char ch : word) {
            if (cur->children.count(ch) == 0) {
                return false;
            } else {
                cur = cur->children[ch];
            }
        }
        
        if (exact_match) {
            return (cur->end) ? true : false;
        } else {
            return true;
        }
    }

private:
    TrieNode* root;
};
