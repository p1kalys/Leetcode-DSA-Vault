class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n=nums.size();
        vector<int>pref_matrix(n);
        vector<int>suf_matrix(n);
        vector<int>res(n);
        
        pref_matrix[0]=1,suf_matrix[n-1]=1;
        for(int i=1; i<n; i++){
            pref_matrix[i]=pref_matrix[i-1]*nums[i-1];
        }

        for(int i=n-2; i>=0; i--){
            suf_matrix[i]=suf_matrix[i+1]*nums[i+1];
        }
        for(int i=0;i<=n-1;i++){
            res[i]=suf_matrix[i]*pref_matrix[i];
        }
        return res;
        
    }
};