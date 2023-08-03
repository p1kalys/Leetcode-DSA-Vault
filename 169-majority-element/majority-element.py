class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x=len(nums)//2
        y=set(nums)
        for i in y:
            if nums.count(i)>x:
                return i