class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int maxi=*max_element(nums.begin(),nums.end());
        int res=INT_MIN;
        int maximum=0;
        for(int i=0; i<nums.size();i++){
            if (nums[i] == maxi){
                maximum++;
                res=max(res,maximum);
            }
            else{
                maximum=0;
            }
        }
        return res;
    }
};