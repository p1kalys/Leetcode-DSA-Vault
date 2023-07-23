class Solution:
        
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10**9 + 7
        def expo(n, p):
            ans = 1
            while p:
                if p & 1:
                    ans = ans * n % mod
                n = n * n % mod
                p >>= 1
            return ans
        v = [0]
        i = 1
        while expo(i, x) < n + 1:
            v.append(expo(i, x))
            i += 1

        size = len(v)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, size):
            newdp = [0] * (n + 1)
            for j in range(n + 1):
                take, notake = 0, 0
                if j >= v[i]:
                    take = dp[j - v[i]]
                notake = dp[j]
                newdp[j] = (take + notake) % mod
            dp = newdp

        return dp[n]


