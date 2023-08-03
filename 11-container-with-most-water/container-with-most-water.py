class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        i=0
        j=n-1
        area=0
        while i<j:
            area=max(area,min(height[i],height[j])*abs(i-j))
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
        return area