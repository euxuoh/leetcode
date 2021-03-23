#include <bits/stdc++.h>

using namespace std;


/**
 * Definition for a binary tree node.
 */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if (preorder.size() != inorder.size()) {
            return nullptr;
        }
        if (preorder.empty()) {
            return nullptr;
        }

        int len = preorder.size();
        for (int i = 0; i < len; ++i) {
            index[inorder[i]] = i;
        }

        return build_tree_from_pre_inorder(preorder, inorder, 0, len-1, 0, len-1);
    }

    TreeNode* build_tree_from_pre_inorder(vector<int>& preorder, vector<int>& inorder, int pre_left, int pre_right, int in_left, int in_right) {
        if (pre_left > pre_right) {
            return nullptr;
        }

        int root_val = preorder[pre_left];
        TreeNode* root = new TreeNode(root_val);
        int root_index = index[root_val];

        root->left = build_tree_from_pre_inorder(preorder, inorder, pre_left+1, pre_left+root_index-in_left, in_left, root_index-1);
        root->right = build_tree_from_pre_inorder(preorder, inorder, pre_left+root_index-in_left+1, pre_right, root_index+1, in_right);

        return root;
    }

    TreeNode* buildTreeFromPostInorder(vector<int>& postorder, vector<int>& inorder) {
        if (postorder.size() != inorder.size()) {
            return nullptr;
        }
        if (postorder.empty()) {
            return nullptr;
        }

        int len = postorder.size();
        for (int i = 0; i < len; ++i) {
            index[inorder[i]] = i;
        }

        return build_tree_from_post_inorder(postorder, inorder, 0, len-1, 0, len-1);
    }

    TreeNode* build_tree_from_post_inorder(vector<int>& postorder, vector<int>& inorder, int post_left, int post_right, int in_left, int in_right) {
        if (post_left > post_right) {
            return nullptr;
        }

        int root_val = postorder[post_right];
        TreeNode* root = new TreeNode(root_val);
        int root_index = index[root_val];

        root->left = build_tree_from_post_inorder(postorder, inorder, post_left, post_left+root_index-in_left-1, in_left, root_index-1);
        root->right = build_tree_from_post_inorder(postorder, inorder, post_left+root_index-in_left, post_right-1, root_index+1, in_right);
        return root;
    }

private:
    unordered_map<int, int> index;
};