class Solution {
    int res;
    void solve(vector<int>& nums, int target, int len, int start_value){
        if (len==nums.size() && start_value==target){
            res++;
            return;
        }
        else if (len==nums.size()){
            return;
        }
        start_value+=nums[len];
        solve(nums,target,len+1,start_value);
        start_value-=2*nums[len];
        solve(nums,target,len+1,start_value);
    }
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        res=0;
        solve(nums,target,0,0);
        return res;
    }
};