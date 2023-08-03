class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        j=0
        n=len(nums)
        res=n+1
        sum=0
        while j<n:
            sum+=nums[j]
            if sum>=target:
                while sum>=target:
                    sum-=nums[i]
                    res=min(res,j-i+1)
                    i+=1
            j+=1
        if res==n+1:
            return 0
        return res
        