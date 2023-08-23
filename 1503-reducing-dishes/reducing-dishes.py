class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        res=0
        satisfaction.sort()
        n=len(satisfaction)
        dp=[[-1]*(n+1) for _ in range(n+1)]

        def f(i, time):
            if i==len(satisfaction):
                return 0
            if dp[i][time] != -1:
                return dp[i][time]

            nt = 0 + f(i+1, time)
            t = satisfaction[i]*time + f(i+1, time+1)
            dp[i][time] = max(t,nt)
            return dp[i][time]

        return f(0, 1)
         