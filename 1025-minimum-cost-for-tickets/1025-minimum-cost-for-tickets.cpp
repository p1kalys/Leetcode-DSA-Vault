class Solution {
public:
    int solve(vector<int>& days, vector<int>& costs, int i, vector<int>& dp) {
        if(i>=days.size()){
            return 0;
        }
        if (dp[i]!=-1){
            return dp[i];
        }
        int res=INT_MAX;
        res = min(res, costs[0]+solve(days,costs, i+1,dp));
        res = min(res, costs[1]+solve(days,costs,upper_bound(days.begin(),days.end(),days[i]+6)-days.begin(),dp));
        res = min(res, costs[2]+solve(days,costs,upper_bound(days.begin(),days.end(),days[i]+29)-days.begin(),dp));
        return dp[i] = res;
    }

    int mincostTickets(vector<int>& days, vector<int>& costs) {
        int n=days.size();
        vector<int>dp(n+1,-1);
        return solve(days, costs, 0, dp);
    }
};