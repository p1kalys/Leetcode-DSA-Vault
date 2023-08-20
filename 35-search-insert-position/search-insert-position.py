class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        ans=len(nums)
        while i<=j:
            m=i+(j-i)//2
            if nums[m]>=target:
                ans=m
                j=m-1
            else:
                i=m+1
        return ans