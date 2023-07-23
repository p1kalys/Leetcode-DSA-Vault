class Solution:
    def isGood(self, nums: List[int]) -> bool:
        maxi=max(nums)
        nums.sort()
        if nums[0]!=1:
            return False
                
        if len(nums)>=2:  
            if len(nums)>2 and maxi!=len(nums)-1:
                return False
            
            if nums[-1]==nums[-2]:
                if nums[-1]==maxi:
                    nums=nums[:-2]
                    for i in range(len(nums)-1):
                        if nums[i]==i+1:
                            continue
                        else:
                            return False
                    return True
                else:
                    return False