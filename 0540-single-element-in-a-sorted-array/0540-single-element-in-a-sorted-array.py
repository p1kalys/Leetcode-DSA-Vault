class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=1
        n=len(nums)
        r=n-2
        if n==1: return nums[0]
        if nums[0]!=nums[1]: return nums[0]
        if nums[n-2]!=nums[n-1]: return nums[n-1]
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            if (mid%2!=0 and nums[mid]==nums[mid-1]) or (mid%2==0 and nums[mid]==nums[mid+1]):
                l=mid+1
            else:
                r=mid-1
        return -1
