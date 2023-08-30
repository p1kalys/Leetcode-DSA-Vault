class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        maxMin = nums[n-1]
        for i in range(n-2,-1,-1):
            parts = ceil(nums[i]/maxMin)
            res += parts-1
            maxMin = nums[i]//parts
        return res