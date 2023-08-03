class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return len(nums)
        k=2
        j=k
        for i in range(k,len(nums)):
            if nums[i]!=nums[j-k]:
                nums[j]=nums[i]
                j+=1
        return j