class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        vector<vector<int>>dp(m+1,vector<int>(n+1,0));

        for(string s:strs){
            int countzero=count(s.begin(),s.end(),'0');
            int countone=s.size()-countzero;
            for(int j=m;j>=countzero;j--){
                for(int k=n; k>=countone;k--){
                    dp[j][k]=max(dp[j-countzero][k-countone]+1,dp[j][k]);
                }
            }
        }
        return dp[m][n];
    }
};