class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        if nums[0]<=nums[-1]:
            flag=True
        else:
            flag=False
        if flag:
            for i in range(1,len(nums)):
                if nums[i-1]<=nums[i]:
                    continue
                else:
                    return False
        else:
            for i in range(1,len(nums)):
                if nums[i-1]>=nums[i]:
                    continue
                else:
                    return False
        return True