class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end());
        int i=0,j=1;
        int res=0;
        while (i<nums.size() && j<nums.size()){
            if (i==j or nums[j]-nums[i]<k){
                j++;
            }
            else if(nums[j]-nums[i]>k){
                i++;
            }
            else{
                res++;
                i++;
                while(i<nums.size() && nums[i]==nums[i-1]){
                    i++;
                }
            }
        }
        return res;
    }
};