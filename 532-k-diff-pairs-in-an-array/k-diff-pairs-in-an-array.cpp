class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        map<int,int>mp;
        for(auto i:nums){
            mp[i]++;
        }
        int res=0;
        for(auto i:mp){
            if(k==0){
                if(i.second>1){
                    res++;
                }
            }
            else if(k>0 && mp.find(k+i.first)!=mp.end()){
                res++;
            }

        }
        return res;
    }
};