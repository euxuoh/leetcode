#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

/**
 * Definition for a binary tree node.
 */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        preorder_helper(root, res);
        return res;
    }

    void preorder_helper(TreeNode* root, vector<int>& res) {
        if (root) {
            res.push_back(root->val);
            preorder_helper(root->left, res);
            preorder_helper(root->right, res);
        }
    }

    vector<int> preorder_iter(TreeNode* root) {
        vector<int> res;
        if (root == nullptr) {
            return res;
        }

        TreeNode* node = root;
        stack<TreeNode*> stk;

        while (true) {
            while (node) {
                res.push_back(node->val);
                stk.push(node);
                node = node->left;
            }

            if (stk.empty()) {
                break;
            }

            node = stk.top()->right;
            stk.pop();
        }

        return res;
    }

    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        inorder_helper(root, res);
        return res;
    }

    void inorder_helper(TreeNode* root, vector<int>& res) {
        if (root) {
            inorder_helper(root->left, res);
            res.push_back(root->val);
            inorder_helper(root->right, res);
        }
    }

    vector<int> inorder_iter(TreeNode* root) {
        vector<int> res;
        if (root == nullptr) {
            return res;
        }

        TreeNode* node = root;
        stack<TreeNode*> stk;

        while (true) {
            while (node) {
                stk.push(node);
                node = node->left;
            }

            if (stk.empty()) {
                break;
            }

            TreeNode* tmp = stk.top();
            stk.pop();
            res.push_back(tmp->val);
            node = tmp->right;            
        }

        return res;
    }

    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;
        postorder_helper(root, res);
        return res;
    }

    void postorder_helper(TreeNode* root, vector<int>& res) {
        if (root) {
            postorder_helper(root->left, res);
            postorder_helper(root->right, res);
            res.push_back(root->val);
        }
    }

    vector<int> postorder_iter(TreeNode* root) {
        vector<int> res;
        if (root == nullptr) {
            return res;
        }

        stack<TreeNode*> stk({root});

        while (!stk.empty()) {
            TreeNode* node = stk.top();
            stk.pop();
            res.push_back(node->val);
            if (node->left) {
                stk.push(node->left);
            }
            if (node->right) {
                stk.push(node->right);
            }
        }

        reverse(res.begin(), res.end());
        return res;

    }

    vector<vector<int>> levelorderTraversal(TreeNode* root) {
        if (root == nullptr) {
            return {};
        }

        vector<vector<int>> res;
        vector<TreeNode*> current(1, root);

        while (!current.empty()) {
            vector<int> value;
            vector<TreeNode*> next_level;
            for (auto node : current) {
                value.push_back(node->val);
                if (node->left) {
                    next_level.push_back(node->left);
                }
                if (node->right) {
                    next_level.push_back(node->right);
                }
            }
            res.push_back(value);
            current = next_level;
        }

        return res;
    }
};