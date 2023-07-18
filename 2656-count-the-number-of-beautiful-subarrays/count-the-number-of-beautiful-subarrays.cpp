class Solution {
public:
    long long beautifulSubarrays(vector<int>& nums) {
        long long ans=0, x=0;
        map<long long, long long>mp;
        mp[0]++;
        for(int i=0; i<nums.size();i++){
            x=x^nums[i];
            if (mp[x]){
                ans+=mp[x];
            }
            mp[x]++;
        }
        return ans;
    }
};