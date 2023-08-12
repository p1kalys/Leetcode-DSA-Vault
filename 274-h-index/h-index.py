class Solution:
    def hIndex(self, c: List[int]) -> int:
        c.sort()
        n=len(c)
        i = 0
        j=n-1
        while i<=j:
            m=i+(j-i)//2
            if c[m]==n-m:
                return c[m]
            elif c[m]>n-m:
                j=m-1
            else:
                i=m+1
        return n-i

        