class Solution {
public:
    bool validPartition(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n,-1);
        return helper(nums, dp, 0, n);
        }
        bool helper(vector<int> &arr, vector<int> &dp, int i, int n) {
        if(i >= n) return true;
        if(dp[i] != -1) return dp[i];
        if(i + 1 < n && arr[i] == arr[i + 1]) {
        dp[i] = helper(arr, dp, i + 2, n);
        if(dp[i]) return true;
        if(i + 2 < n && arr[i] == arr[i +2]) {
        dp[i] = helper(arr, dp, i + 3, n);
        if(dp[i]) return true;
        }
        }
        if(i + 2 < n && arr[i + 1] - arr[i] == 1 && arr[i+2] - arr[i] == 2) {
        dp[i] = helper(arr, dp, i+3, n);
        if(dp[i]) return true;
        }
        return dp[i] = false; 
    }
};