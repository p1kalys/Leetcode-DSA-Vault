class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        vector<int> ans(nums.size(),0);
        int n=nums.size();
        int sum=0;
        vector<int> leftsum;
        vector<int> rightsum(nums.size(),0);
        leftsum.push_back(0);
        sum+=nums[0];
        for(int i=1;i<nums.size();i++)
        {
            leftsum.push_back(sum);
            sum+=nums[i];
        }
        sum=0;
        rightsum[n-1]=0;
        sum+=nums[n-1];
        for(int i=n-2;i>=0;i--)
        {
            rightsum[i]=sum;;
            sum+=nums[i];
        }
        for(int i=0;i<n;i++)
        {
            ans[i]=abs(leftsum[i]-rightsum[i]);
        }
        return ans;
    }
};