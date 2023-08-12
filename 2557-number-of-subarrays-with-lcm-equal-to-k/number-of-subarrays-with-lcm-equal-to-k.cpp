class Solution {
public:

    int subarrayLCM(vector<int>& nums, int k) {
        int n=nums.size();
        int ans=0;
        for(int i=0;i<n;i++){
            int cur=1;
            for(int j=i;j<n;j++){
                cur=lcm(cur,nums[j]);
                ans+=(cur==k)?1:0;
                if(cur>k) break;
            }
        }
        return ans;
    }
};