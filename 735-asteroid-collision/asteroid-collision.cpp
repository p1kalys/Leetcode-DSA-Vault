class Solution {
public:
    vector<int> asteroidCollision(vector<int>& nums) {
        vector<int>st;
        for(int i=0; i<nums.size(); i++){
            if (nums[i]>0 or st.empty() or st.back()<0){
                st.push_back(nums[i]);
            } 
            else if (st.back()<=(-nums[i])){
                if (st.back()<-nums[i]){
                    i--;
                }
                st.pop_back();
            }
        }
        return st;
    }
};