class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        if k==n or n==1:
            return n
        l=0
        res=0
        maxf=0
        freq={}
        flips=0
        for r in range(n):
            if s[r] in freq:
                freq[s[r]]+=1
            else:
                freq[s[r]]=1
            maxf = max(maxf,freq[s[r]])
            flips=r-l+1-maxf
            if flips<=k:
                res=max(res,r-l+1)
            else:
                freq[s[l]]-=1
                l+=1
        return res