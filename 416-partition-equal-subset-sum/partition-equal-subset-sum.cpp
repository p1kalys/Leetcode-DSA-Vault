class Solution {
    int solve(vector<int>&nums, int index, int target, vector<vector<int>>&dp){
        if (target==0){
            return true;
        }
        if (index==0){
            return nums[0]==target;
        }
        if(dp[index][target]!=-1){
            return dp[index][target];
        }
        int notTake=solve(nums,index-1,target,dp);
        int take=false;
        if (nums[index]<=target){
            take=solve(nums,index-1,target-nums[index],dp);
        }
        return dp[index][target]=take|notTake;
    }
public:
    bool canPartition(vector<int>& nums) {
        int sum=0;
        for(auto i: nums){
            sum+=i;
        }
        if (sum%2!=0){
            return false;
        }
        int n=nums.size();
        vector<vector<int>>dp(n, vector<int>(sum/2+1,-1));
        return solve(nums,n-1,sum/2,dp);
    }
};