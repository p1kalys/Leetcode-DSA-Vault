class Solution {
    vector<vector<int>> ans;
    void f(int cur, vector<int>& nums, vector<int> res){
        if (cur<0) {
            ans.push_back(res);
            return;
        }

        f(cur-1,nums,res);
        res.push_back(nums[cur]);
        f(cur-1,nums,res);
    }
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int>res;
        f(nums.size()-1,nums,res);
        return ans;
    }
};