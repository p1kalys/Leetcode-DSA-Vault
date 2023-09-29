class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        
        def f(mid):
            hour = 0
            for i in range(len(piles)):
                hour+=math.ceil(piles[i]/mid)
            return hour

        while l<=r:
            mid = l+(r-l)//2
            total = f(mid)
            if total <= h:
                r = mid-1
            else:
                l=mid+1
        return l