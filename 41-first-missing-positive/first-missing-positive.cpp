class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; i++){
            int element = nums[i];
            if (element >= 1 && element <=n){
                int pos = element - 1;
                if (nums[pos] != element){
                    swap(nums[pos],nums[i]);
                    i--;
                }
            }
        }
        for(int i = 0; i < n; i++){
            if (nums[i] != i+1){
                return i+1;
            }
        }
        return n+1;
    }
};