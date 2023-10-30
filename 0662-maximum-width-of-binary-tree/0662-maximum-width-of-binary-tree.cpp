/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int widthOfBinaryTree(TreeNode* root) {
       if (!root) return 0;
int ans = 0;
queue<pair<TreeNode*, uint64_t>> q;
q.push({root, 0});

while (!q.empty()) {
    int size = q.size();
    uint64_t first, last;  // Initialize first and last within the loop

    for (int i = 0; i < size; i++) {

        uint64_t cur_id = q.front().second;  // Get the current ID
        TreeNode* node = q.front().first;
        q.pop();

        if (i == 0) first = cur_id;  // Update first ID
        if (i == size - 1) last = cur_id; // Update last ID

        if (node->left) {
            q.push({node->left, cur_id * 2 + 1});
        }
        if (node->right) {
            q.push({node->right, 2 * cur_id + 2});
        }
    }
    ans = max(ans, static_cast<int>(last - first + 1));
}
return ans;
 
    }
};