class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int res=1;
        int cur=1;
        if(nums.size()==0 || nums.size()==1){
            return nums.size();
        }
        set<int>s;
        for(auto i:nums){
            s.insert(i);
        }
        auto fast=s.begin();
        auto slow=s.begin();
        fast++;
        while (fast!=s.end()){
            if (*fast==*slow+1){
                cur+=1;
            }
            else{
                res=max(res,cur);
                cur=1;
            }
            fast++;
            slow++;
        }
        return max(cur,res);
    }
};