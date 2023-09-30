class Solution {
public:
    int minOperations(vector<int>& nums) {
        map<int,int>mp;
        for (auto i:nums){
            mp[i]++;
        }
        int moves=0;
        for (auto it:mp){
            int f= it.second;
            if(f==1){
                return -1;
            }
            moves+=f/3;
            if(f%3){
                moves++;
            }
        }
        return moves;
    }
};