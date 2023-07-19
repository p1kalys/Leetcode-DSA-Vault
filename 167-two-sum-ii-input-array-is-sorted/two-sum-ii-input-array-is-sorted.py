class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start=0
        end=len(nums)-1
        while (start<end):
            s=nums[start]+nums[end]
            if s==target:
                return [start+1,end+1]
            elif s<target:
                start+=1
            else:
                end-=1
        return []