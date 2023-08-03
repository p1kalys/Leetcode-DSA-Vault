class Solution:
    def trap(self, height: List[int]) -> int:
        s=0
        left=0
        right=len(height)-1
        maxL=0
        maxR=0
        while left<=right:
            if height[left]<=height[right]:
                if height[left] > maxL:
                    maxL=height[left]
                else:
                    s+=maxL-height[left]
                left+=1
            else:
                if height[right]>=maxR:
                    maxR=height[right]
                else:
                    s+=maxR-height[right]
                right-=1
        return s
