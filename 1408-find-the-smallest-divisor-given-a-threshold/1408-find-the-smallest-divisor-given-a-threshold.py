import math
def calculate(nums, div):
    Sum=0
    for i in range(len(nums)):
        Sum+=math.ceil(nums[i]/div)
    return Sum

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        totalsum=0
        low=1
        high=max(nums)
        while low<=high:
            mid=(low+high)//2
            totalsum=calculate(nums,mid)
            if totalsum<=threshold:
                high=mid-1
            else:
                low=mid+1
        return low
