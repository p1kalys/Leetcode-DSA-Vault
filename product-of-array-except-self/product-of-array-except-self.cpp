class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n=nums.size();
        vector<int>res(n);
        res[0]=1;
        int suf_prod=1;
        for(int i=1; i<n; i++){
            res[i]=res[i-1]*nums[i-1];
        }
        for(int i=n-1;i>=0;i--){
            res[i]=suf_prod*res[i];
            suf_prod=suf_prod*nums[i];
        }
        return res;
        
    }
};