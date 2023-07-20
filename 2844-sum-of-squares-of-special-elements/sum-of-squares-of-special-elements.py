class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        for i in range(len(nums)):
            if n%(i+1)==0:
                ans+=(nums[i]*nums[i])
        return ans