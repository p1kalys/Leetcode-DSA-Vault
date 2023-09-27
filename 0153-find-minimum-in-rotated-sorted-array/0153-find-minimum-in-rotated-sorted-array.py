class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<=nums[len(nums)-1]:
            return nums[0]
        s=0
        e=len(nums)-1
        while s<=e:
            mid=s+(e-s)//2
            if mid!=0 and nums[mid]<nums[mid-1]:
                return nums[mid]
            elif nums[mid]<nums[mid+1] and nums[mid]<nums[mid-1]:
                return nums[mid]
            elif nums[mid]>=nums[0]:          
                s=mid+1
            else:
                e=mid-1
        return -1