class Solution {
public:
    vector<int> findLonely(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<int>ans;
        if (nums.size()<=1)return nums;
        for(int i=0;i<nums.size();i++){
            if (i==0){
                if (nums[i+1]-nums[i]>1){
                    ans.push_back(nums[i]);
                }           
            }
            else if (nums.size()-1 ==i){
                if(nums[i]-nums[i-1]>1)ans.push_back(nums[i]);
            } 
            else {
                if (nums[i]-nums[i-1]>1 and nums[i+1]-nums[i]>1){
                    ans.push_back(nums[i]);
                }
            }            
        }
        return ans;
    }
};