class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def back(nums,ans,temp):
            ans.append(temp)
            for i in range(len(nums)):
                if i!=0 and nums[i]==nums[i-1]:
                    continue
                back(nums[i+1:], ans, temp+[nums[i]])
        ans=[]
        back(sorted(nums),ans,[])
        return ans