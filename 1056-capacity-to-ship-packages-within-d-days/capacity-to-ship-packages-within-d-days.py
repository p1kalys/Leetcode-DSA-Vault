def isPossible( mid, weights, days):
        daysPassed=1
        total=0
        for weight in weights:
            total+=weight
            if total>mid:
                total=weight
                daysPassed+=1
            if daysPassed>days:
                return False
        return True
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo=max(weights)
        hi=sum(weights)
        while lo<hi:
            mid=lo+(hi-lo)//2
            if isPossible(mid,weights,days):
                hi=mid
            else:
                lo=mid+1
        return lo
