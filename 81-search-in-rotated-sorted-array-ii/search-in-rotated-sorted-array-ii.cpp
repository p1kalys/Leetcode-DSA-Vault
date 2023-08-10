class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int l=0;
        int r=nums.size()-1;
        while(l<=r){
            int m=(l+r)/2;
            if(nums[m]==target) return true;
            if(nums[m]==nums[l] && nums[m]==nums[r]){
                r--;
                l++;
            }
            else if (nums[l]<=nums[m]){
                if (nums[m]>target && nums[l]<=target) r=m-1;
                else l=m+1;
            }
            else{
                if(nums[m]<target && nums[r]>=target) l=m+1;
                else r=m-1;
            }
        }
        return false;
    }
};