class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n=len(nums)
        res=len(nums)
        i=0
        j=(n+1) //2

        while i<n//2 and j<n:
            if nums[i]<nums[j]:
                res-=2
            i+=1
            j+=1

        return res