class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        diff=0
        for i in range(1,len(nums)):
            diff=max(diff, nums[i]-nums[i-1])
        return diff