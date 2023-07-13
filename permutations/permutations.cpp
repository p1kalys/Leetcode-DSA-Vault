class Solution {
    vector<vector<int>>ans;
    void f(int cur, vector<int>nums){
        if (cur==nums.size()){
            ans.push_back(nums);
            return;
        }
        for (int i=cur; i<nums.size(); i++){
            swap(nums[cur],nums[i]);
            f(cur+1,nums);
            swap(nums[cur],nums[i]);
        }
    }
public:
    vector<vector<int>> permute(vector<int>& nums) {
        f(0,nums);
        return ans;
    }
};