// leetcode create tree

#include <bits/stdc++.h>

using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(): val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right): val(x), left(left), right(right) {}
};

TreeNode* create_tree(vector<string> nodes) {
    if (nodes.size() == 0) {
        return nullptr;
    }
    queue<TreeNode*> q;
    TreeNode* root = new TreeNode(std::stoi(nodes[0]));
    q.push(root);
    int i = 1;
    while (i < nodes.size()) {
        int cur_size = q.size();
        for (int j = 0; j < cur_size; ++j) {
            TreeNode* node = q.front();
            q.pop();
            if (nodes[i] != "null") {
                node->left = new TreeNode(std::stoi(nodes[i]));
                q.push(node->left);
            }
            i++;
            if (nodes[i] != "null") {
                node->right = new TreeNode(std::stoi(nodes[i]));
                q.push(node->right);
            }
            i++;
        }
    }
    return root;
}

int main() {
    // Write C++ code here

    // 手动建树
    // TreeNode* root = new TreeNode(5);
    // root->left = new TreeNode(4);
    // root->left->left = new TreeNode(11);
    // root->left->left->left = new TreeNode(7);
    // root->left->left->right = new TreeNode(2);
    
    // root->right = new TreeNode(8);
    // root->right->left = new TreeNode(13);
    // root->right->right = new TreeNode(4);
    // root->right->right->left = new TreeNode(5);
    // root->right->right->right = new TreeNode(1);
    
    // 自动建树
    vector<std::string> nodes = {"5", "4", "8", "11", "null", "13", "4", "7", "2", "null", "null", "5", "1"};
    TreeNode* root = create_tree(nodes);
}
