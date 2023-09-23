class Solution {
public:
    bool check(vector<int>& nums) {
        int x=0;
        for(int i=0;i<nums.size();i++){
            if(nums[(i+1)%nums.size()]<nums[i]){
                x++;
            }
        }
        if(x<2){
            return true;
        }
        else 
        return false;
        
    }
};
