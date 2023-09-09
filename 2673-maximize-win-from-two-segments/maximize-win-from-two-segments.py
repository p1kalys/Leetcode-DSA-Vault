class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        N = len(prizePositions)
        dp = [0] * (N + 1)
        l = 0
        ans = 0
        for r in range(N):
            while prizePositions[l] + k < prizePositions[r]:
                l += 1
            dp[r + 1] = max(dp[r], r - l + 1)
            ans = max(ans, dp[l] + r - l + 1)
            
        return ans