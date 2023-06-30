class Solution {
public:
    int solve(vector<int>& nums, int i, int j){
        if(i > j)
        return 0;
        
        if(i == j)
        return nums[j];

        int p1 = nums[i] + min(solve(nums, i+2, j), solve(nums, i+1, j-1));
        int p2 = nums[j] + min(solve(nums, i+1, j-1), solve(nums, i, j-2));

        return max(p1, p2);
    }
    bool PredictTheWinner(vector<int>& nums) {
        int i = 0;
        int temp = 0;
        int j = nums.size()-1;

        for(auto it:nums){
            temp += it;
        }

        int p1 = solve(nums, i, j);
        int p2 = temp-p1;

        return p1 >= p2;
        
    }
};