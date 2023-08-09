class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        if p==0:
            return 0
        def isvalid(threshold):
            i=0
            cnt=0
            while i<len(nums)-1:
                if abs(nums[i]-nums[i+1]) <=threshold:
                    cnt+=1
                    i+=2
                else:
                    i+=1
                if cnt==p:
                    return True
            return False
        l=0
        r,res=10**9,10**9
        while l<=r:
            m=l+(r-l)//2
            if isvalid(m):
                res=m
                r=m-1
            else:
                l=m+1
        return res