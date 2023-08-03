class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        pre=0
        res=0
        for i in range(len(nums)):
            pre+=nums[i]
            res=max(res,ceil(pre/(i+1)))
        return res