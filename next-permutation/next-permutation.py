class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s=len(nums)-2
        j=len(nums)-1
        while s>=0 and nums[s]>=nums[s+1]:
            s-=1
        if s<0:
            nums.reverse()
        else:   
            while j>s and nums[j]<=nums[s]:
                j-=1
            nums[j],nums[s]=nums[s],nums[j]
            nums[s+1:]=reversed(nums[s+1:])  
                    
                
