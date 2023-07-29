class Solution:
    def countPrimes(self, n: int) -> int:
        seen, ans = [0] * n, 0
        for num in range(2, n):
            if seen[num]: continue
            ans += 1
            for i in range(num*num,n,num):
                seen[i]=True
        return ans