class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod=1
        for i in nums:
            if i==0:
                return 0
            prod=prod*i
        if prod>0:
            return 1
        else:
            return -1