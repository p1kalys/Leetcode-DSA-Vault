class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m=0
        for i in range(len(nums)):
            m=max(m,nums[i]+i)
            if(m>=len(nums)-1):
                return True
            if(m==i):
                return False
        return True