class Solution:
    def trailingZeroes(self, n: int) -> int:
        c,i=0,5
        while i<=n:
            c+=n//i
            i*=5
        return c
