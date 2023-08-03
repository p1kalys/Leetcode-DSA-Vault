class Solution {
public:
    int minimizeArrayValue(vector<int>& nums) {
        long long answer=0,presum=0;
        for(int i=0;i<nums.size();i++){
            presum+=nums[i];
            answer=max(answer, (presum+i)/(i+1));
        } 
        return answer;
    }
};