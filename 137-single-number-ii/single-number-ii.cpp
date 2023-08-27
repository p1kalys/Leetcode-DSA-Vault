class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res=0;
        for(int i=0;i<32;i++){
            int bit=1<<i;
            int c=0;
            for(int j=0;j<nums.size();j++){
                if (nums[j]&bit){
                c++;
                }
            }
            if (c%3){
                res=res|bit;
            }
        }
        return res;
    }
};
