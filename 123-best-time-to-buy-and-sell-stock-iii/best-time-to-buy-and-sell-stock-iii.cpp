class Solution 
{
    int f(vector<int> &prices,bool buy,int index,vector<vector<vector<int>>> &dp,int cap)
    {
        //base case
        //no stock remaining
        if(index == prices.size()) return 0;
        if(cap == 0) return 0;

        if(dp[index][buy][cap] != -1) return dp[index][buy][cap];

        //buy or sell 
        //pick or no pick  
        if(buy)
        {
            int buy_pick = -prices[index] + f(prices, 0, index+1, dp, cap);
            int buy_noPick = 0 + f(prices, 1, index+1, dp, cap);
            return dp[index][buy][cap] = max(buy_pick, buy_noPick);
        }
        // else sell
        
            int sell_pick = prices[index] + f(prices, 1, index+1, dp, cap-1);
            int sell_noPick = 0 + f(prices, 0, index+1, dp, cap);
            return dp[index][buy][cap] = max(sell_pick, sell_noPick);
        

    }
    
public:
    int maxProfit(vector<int>& prices) 
    {
        int n=prices.size();
        int cap = 2;
        vector<vector<vector<int>>> dp (n, vector<vector<int>>(2, vector<int> (cap+1,-1)));
        return f(prices, 1, 0,dp,cap);   
    }
};