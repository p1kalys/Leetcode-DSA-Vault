class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo=0
        hi=len(nums)-2
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if nums[mid]==nums[mid^1]:
                lo=mid+1
            else:
                hi=mid-1
        return nums[lo]