class Solution {
public:
    vector<int> getRow(int n) {
        if(n==0) return {1};
        if (n==1) return {1,1};

        vector<int>dp ={1,1};
        for(int i=2; i<=n; i++){
            vector<int>temp(dp.size()+1,1);
            for(int j=1;j<i;j++) {
                temp[j]=dp[j]+dp[j-1];
            }
            dp=temp;
        }
        return dp;
    }
};