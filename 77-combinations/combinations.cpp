class Solution {
    void helper(int i, int n, int k, vector<int>&slate, vector<vector<int>>&ans){
        if (k==slate.size()){
            ans.push_back(slate);
            return;
        }
        if (i==n+1){
            return;
        }
        
        slate.push_back(i);
        helper(i+1,n,k,slate,ans);
        slate.pop_back();
        helper(i+1,n,k,slate,ans);

    }
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>>ans;
        vector<int>slate;
        helper(1,n,k,slate,ans);
        return ans;
    }
};