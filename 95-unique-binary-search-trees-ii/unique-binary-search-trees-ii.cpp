class Solution {
public:
    vector<TreeNode*> generateTrees(int n) {
        vector<vector<vector<TreeNode*>>> v(n + 1, vector<vector<TreeNode*>>(n + 1));
        return dfs(v, 1, n);
    }
    vector<TreeNode*> dfs(vector<vector<vector<TreeNode*>>>& v, int l, int r){
        if (l > r) return {nullptr};
        if (l == r) {
            TreeNode* node = new TreeNode(l);
            return {node};
        }
        if (v[l][r].empty()){
            for (int i = l; i <= r; ++i){
                vector<TreeNode*> leftTrees = dfs(v, l, i - 1),
                rightTrees = dfs(v, i + 1, r);
                for (auto& left : leftTrees)
                    for (auto& right: rightTrees){
                        TreeNode* node = new TreeNode(i, left, right);
                        v[l][r].push_back(node);
                    }
            }
        }        
        return v[l][r];
    }
};