class Solution {
public:
    int findMin(vector<int>& nums) {
        int s=0,e=nums.size()-1;
        if(nums[s]<=nums[e]){
            return nums[s];
        }
        while(s<=e){
            int mid=s+(e-s)/2;
            if(mid!=0 && nums[mid]<nums[mid-1]){
                return nums[mid];
            }
            else if(nums[mid]<nums[mid+1] && nums[mid]<nums[mid-1]){
                return nums[mid];
            }
            else if(nums[mid]>=nums[0]){
                s=mid+1;
            }
            else{
                e=mid-1;
            }
        }
        return -1;
    }
};