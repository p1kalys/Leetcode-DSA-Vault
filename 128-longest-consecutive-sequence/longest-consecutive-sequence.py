class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        ans=1
        if len(nums)==0:
            return 0
        c=1
        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1]:
                c+=1
                ans=max(ans,c)
            elif nums[i]==nums[i+1]:
                continue
            else:
                c=1
        return ans