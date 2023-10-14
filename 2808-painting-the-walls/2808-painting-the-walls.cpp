class Solution {
public:
    int solve(vector<int> &cost, vector<int> &time, int n, int index, int walls, vector<vector<int>> &dp) {
        if (walls <= 0) return 0;
        if (index >= n) return 1e9;
        int t = time[index] + 1;
        if (dp[index][walls] != -1) return dp[index][walls];
        long long take = cost[index] + solve(cost, time, n, index + 1, walls - t, dp);
        long long not_take = solve(cost, time, n, index + 1, walls, dp);
        return dp[index][walls] = min(take, not_take); 
    }

    int paintWalls(vector<int>& cost, vector<int>& time) {
        int n = cost.size();
        vector<vector<int>> dp(n, vector<int>(n + 1, -1));
        return solve(cost, time, n, 0, n, dp);
    }
};