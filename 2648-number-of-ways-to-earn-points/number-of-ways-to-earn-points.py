class Solution:    
    def f(self, target, types, index, dp):
        MOD = 1e9 + 7
        if (index == len(types)):
            if target == 0: 
                return 1
            return 0
        if dp[index][target] != -1:
            return dp[index][target]
        ans = 0
        #not take
        ans = (ans + self.f(target, types, index + 1, dp) % MOD) % MOD
        #take
        for j in range(1, types[index][0] + 1):
            if target >= j * types[index][1]:
                ans = (ans + self.f(target - j * types[index][1], types, index  + 1, dp) % MOD) % MOD
            else:
                break
        dp[index][target] = int(ans % MOD)
        return dp[index][target]

    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        dp = [[-1] * (target + 1) for _ in range(len(types))]
        return self.f(target, types, 0, dp)