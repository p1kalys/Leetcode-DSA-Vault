class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_d=float('inf')
        res=0
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                s=nums[i]+nums[j]+nums[k]
                if s==target:
                    return target
                elif s<target:
                    if target-s<min_d:
                        min_d=target-s
                        res=s
                    j+=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                else:
                    if s-target<min_d:
                        min_d=s-target
                        res=s
                    k-=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return res