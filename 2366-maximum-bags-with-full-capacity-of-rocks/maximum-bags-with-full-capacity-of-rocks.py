class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n=len(capacity)
        for i in range(n):
            capacity[i]-=rocks[i]
        capacity.sort()
        res=0
        i=0
        while additionalRocks and i<n:
            if additionalRocks<capacity[i]:
                break
            additionalRocks-=capacity[i]
            res+=1
            i+=1
        return res