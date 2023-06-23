class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        r=n
        while(r):
            if (r%2==1):
                c+=1
            r>>=1
        return c
        