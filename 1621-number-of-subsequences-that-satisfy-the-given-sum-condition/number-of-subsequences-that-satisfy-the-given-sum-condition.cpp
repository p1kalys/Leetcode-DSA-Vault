#define MOD 1000000007
class Solution {
    long long f(int N,int R)
    {
       //Your code here
       if (N==0){
            return 0;
       }
       if (R==0){
            return 1;
       }
       if (R%2==0){
            long long int ans=f(N,R/2);
            return (ans%MOD * ans%MOD)%MOD;
       }
       else{
            long long int ans=f(N,(R-1)/2);
            return (ans%MOD * ans%MOD * N%MOD)%MOD;
       }
        
    }
public:
    int numSubseq(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        int n=nums.size();
        int ans=0;
        int l=0;
        int r=n-1;
        while(l<=r){
            if (nums[l]+nums[r]<=target){
                ans+=(f(2,r-l));
                ans%=MOD;
                l++;
            }
            else{
                r--;
            }
        }
        return ans%MOD;
    }
};