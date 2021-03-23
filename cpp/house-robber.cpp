#include <bits/stdc++.h>

using namespace std;


/**
 * Definition for a binary tree node.
 */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.empty()) return 0;

        int first = 0, second = 0;

        for (int num : nums) {
            int tmp = max(second, first+num);
            first = second;
            second = tmp;
            cout << first << second << tmp << endl;
        }

        return second;
    }

    // 213
    int rob2(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) {
            return nums[0];
        }
        int amont1 = rob2_helper(nums, 0, n-2);
        int amont2 = rob2_helper(nums, 1, n-1);
        return max(amont1, amont2);
    }

    int rob2_helper(vector<int>& nums, int start, int end) {
        int prev = 0, cur = 0;

        for (int i = start; i <= end; ++i) {
            int tmp = max(cur, prev+nums[i]);
            prev = cur;
            cur = tmp;
        }

        return cur;
    }

    int rob(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }

        if (map.count(root)) {
            return map[root];
        }

        int rob_cur = root->val + \
            (root->left ? rob(root->left->left)+rob(root->left->right) : 0) + \
            (root->right ? rob(root->right->left)+rob(root->right->right) : 0);
        int rob_not = rob(root->left) + rob(root->right);

        int res = max(rob_cur, rob_not);
        map[root] = res;
        
        return res;
    }

private:
    unordered_map<TreeNode*, int> map;
};
