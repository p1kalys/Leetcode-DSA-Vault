/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
  public:
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder) {
        unordered_map<int, int> m;
        int index = 0;

        for (int i = 0; i < inorder.size(); i++)
            m[inorder[i]] = i;

        return createNode(preorder, index, 0, inorder.size() - 1, m);
    }

    TreeNode *createNode(vector<int> &preorder, int &index, int s, int e,
                         unordered_map<int, int> &m) {
        if (s > e)
            return NULL;

        int i = m[preorder[index]];

        auto *node = new TreeNode(preorder[index++]);

        node->left = createNode(preorder, index, s, i - 1, m);
        node->right = createNode(preorder, index, i + 1, e, m);

        return node;
    }
};