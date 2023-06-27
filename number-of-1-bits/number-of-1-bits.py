class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        while(n):
            if (n%2==1):
                c+=1
            n>>=1
        return c
        