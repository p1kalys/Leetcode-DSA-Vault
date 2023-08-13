class Solution:
    def maxsum(self, nums: List[int]) -> int:
        cursum=0
        subarray_sum=float('-inf')
        for i in range(len(nums)):
            if cursum<0 :
                cursum=0
            cursum+=nums[i]
            subarray_sum=max(subarray_sum,cursum)
        return subarray_sum
    def minsum(self, nums: List[int]) -> int:
        cursum=0
        subarray_sum=float('inf')
        for i in range(len(nums)):
            if cursum>0 :
                cursum=0
            cursum+=nums[i]
            subarray_sum=min(subarray_sum,cursum)
        return subarray_sum

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        flag=True
        ans=float('-inf')
        for i in range(len(nums)):
            if nums[i]>=0:
                flag=False
                break
            ans=max(ans,nums[i])
        if flag:
            return ans
        res1=self.maxsum(nums)
        sub=0
        for i in range(len(nums)):
            sub+=nums[i]
        
        res2=sub-self.minsum(nums)
        res=max(res1,res2)
        return res