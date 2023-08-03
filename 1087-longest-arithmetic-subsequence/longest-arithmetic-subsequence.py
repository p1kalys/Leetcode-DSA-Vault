class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        for i in range(n):
            for j in range(i):
                diff = nums[j] - nums[i]
                dp[i][diff] = dp[j].get(diff, 1) + 1
                ans = max(ans, dp[i][diff])
        return ans