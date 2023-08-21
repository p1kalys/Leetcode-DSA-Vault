class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        def f(index, nums, product,count):
            if index==len(nums):
                if count==0:
                    return float('-inf')
                return product
            take=f(index+1, nums, product*nums[index],count+1)
            not_take=f(index+1,nums, product,count)
            return max(take,not_take)
        return f(0,nums,1,0)
