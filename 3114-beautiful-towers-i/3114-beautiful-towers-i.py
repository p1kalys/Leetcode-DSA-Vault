class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n=len(maxHeights)
        s=0
        ans=0
        for i in range(n):
            peak = maxHeights[i]
            s+=peak
            for j in range(i-1,-1,-1):
                if maxHeights[j]<=peak:
                    s+=maxHeights[j]
                    peak = maxHeights[j]
                else:
                    s+=peak

            peak = maxHeights[i]
            for k  in range(i+1,n):
                if maxHeights[k]<=peak:
                    s+=maxHeights[k]
                    peak=maxHeights[k]
                else:
                    s+=peak
            ans=max(s,ans)
            s=0
        return ans