class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = 0
        for i in nums:
            target+=i

        target-=x

        left =0
        cursum =0
        maxlength=-1
        n=len(nums)
        for i in range(len(nums)):
            cursum+=nums[i]
            while cursum>target and left<=i:
                cursum-=nums[left]
                left+=1
            if cursum==target:
                maxlength=max(maxlength, i-left+1)
        return n-maxlength if maxlength!=-1 else -1 