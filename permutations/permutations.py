def helper(index,nums,res):
    if index==len(nums):
        res.append(nums[:])
        return
    for i in range(index,len(nums)):
        nums[i],nums[index]=nums[index],nums[i]
        helper(index+1,nums,res)
        nums[i],nums[index]=nums[index],nums[i]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        helper(0,nums,res)
        return res
        