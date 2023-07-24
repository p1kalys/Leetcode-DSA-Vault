class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans=[]
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                ans.append(nums[i])
        for i in range(1,len(nums)+1):
            if i in nums:
                continue
            else:
                ans.append(i)
        return ans