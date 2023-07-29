class Solution:
    def mostPoints(self, Q: List[List[int]]) -> int:
        n = len(Q)
        dp = [0] * n
        dp[n-1] = Q[n-1][0]
        for i in range(n-2, -1, -1):
            not_take = dp[i+1]
            take = 0
            if i+Q[i][1]+1 < n:
                take = Q[i][0] + dp[i+Q[i][1]+1]
            else:
                take = Q[i][0]
            dp[i] = max(take, not_take)
        return dp[0]