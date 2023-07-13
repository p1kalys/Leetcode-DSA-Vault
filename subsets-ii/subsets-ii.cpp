class Solution {
    set<vector<int>> ans;
    void f(int cur, vector<int>& nums, vector<int> res){
        if (cur<0) {
            ans.insert(res);
            return;
        }

        f(cur-1,nums,res);
        res.push_back(nums[cur]);
        f(cur-1,nums,res);
    }
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<int>res;
        sort(nums.begin(),nums.end());
        f(nums.size()-1,nums,res);
        vector<vector<int>>final_res;
        for (auto it: ans){
            final_res.push_back(it);
        }        
        return final_res;
    }
};