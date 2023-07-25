class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        maxi=2
        if len(points)<=2:
            return len(points)
        for i in points:
            freq={}
            x1=i[0]
            y1=i[1]
            for j in points:
                if i==j:
                    continue
                
                x2=j[0]
                y2=j[1]
                if x2-x1 ==0:
                    slope=float('inf')
                else:
                    slope=math.atan2(y2-y1, x2-x1)
                freq[slope]=freq.get(slope,0)+1
            for key,value in freq.items():
                maxi=max(maxi,value+1)
        return maxi