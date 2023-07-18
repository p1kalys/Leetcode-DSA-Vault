class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*n
        for i in range(n):
            dp[i]=nums[i]
        for i in range(n):
            for j in range(i-1):
                dp[i]=max(dp[i],dp[j]+nums[i])
        return max(dp)