class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 1
        a=nums[0]
        res=0
        for i in nums:
            a&=i
        if a>0:
            return 1
        a2=nums[0]
        for i in range(len(nums)):
            a2&=nums[i]
            if a==a2:
                res+=1
                if i<n-1:
                    a2=nums[i+1]
        return res