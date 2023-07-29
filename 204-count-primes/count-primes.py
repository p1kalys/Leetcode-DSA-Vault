class Solution:
    def countPrimes(self, n: int) -> int:
        seen, ans = [0] * n, 0
        for num in range(2, n):
            if seen[num]: continue
            ans += 1
            seen[num*num:n:num] = [1] * ((n - 1) // num - num + 1)
        return ans