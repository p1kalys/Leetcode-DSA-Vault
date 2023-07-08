class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        ans=[]
        if k==1:
            return 0
        for i in range(1,len(weights)):
            ans.append(weights[i-1]+weights[i])
        ans.sort()
        l=0
        r=0
        for i in range(k-1):
            l+=ans[i]
            r+=ans[len(ans)-1-i]
        return r-l
            