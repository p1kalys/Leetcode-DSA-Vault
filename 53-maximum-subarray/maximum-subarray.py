class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum=0
        subarray_sum=float('-inf')
        for i in range(len(nums)):
            if cursum<0 :
                cursum=0
            cursum+=nums[i]
            subarray_sum=max(subarray_sum,cursum)
        return subarray_sum