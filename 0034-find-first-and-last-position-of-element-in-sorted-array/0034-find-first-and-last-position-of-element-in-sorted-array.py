def first_position(nums, target):
    lo=0
    hi=len(nums)-1
    res=-1
    while lo<=hi:
        mid=(lo+hi)//2
        if nums[mid]>target:
            hi=mid-1
        elif nums[mid]<target:
            lo=mid+1
        else:
            res=mid
            hi=mid-1
    return res
    

def last_position(nums, target):
    lo=0
    res=-1
    hi=len(nums)-1
    while lo<=hi:
        mid=(lo+hi)//2
        if nums[mid]>target:
            hi=mid-1
        elif nums[mid]<target:
            lo=mid+1
        else:
            res=mid
            lo=mid+1
    return res
    
def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return first_and_last_position(nums, target)