class Solution:
    def smallestGoodBase(self, n: str) -> str:
        res,n=math.inf,int(n)
        for i in range(64):
            l,r=2,n
            while l<=r:
                mid,tmp=(l+r)//2,0
                for j in range(i+1):
                    tmp+=pow(mid,j)
                    if tmp>n:break
                if tmp<n:
                    l=mid+1
                elif tmp>n:
                    r=mid-1
                else:
                    res=min(res,mid)
                    break
        return str(res)