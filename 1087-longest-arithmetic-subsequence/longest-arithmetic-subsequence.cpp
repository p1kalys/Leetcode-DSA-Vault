class Solution {
public:
    int longestArithSeqLength(vector<int>& nums) {
        int n=nums.size();
        if(n<=2)
            return n;

        // //Step 1 : Create Map
        unordered_map<int,int>dp[n+1];

        int ans=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<i;j++){
                int diff=nums[i]-nums[j];
                int count=1;

                //Checking if answer already present
                if(dp[j].count(diff)){
                    //Put it in count
                    count = dp[j][diff];
                }
                dp[i][diff]=1+count;  // 1----> Current element ko include karna hai
                ans=max(ans,dp[i][diff]);
            }
        }
        return ans;
    }
};