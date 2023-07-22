class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res=""
        for i in nums:
            i=str(i)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if str(nums[i])+str(nums[j]) > str(nums[j])+str(nums[i]): #comparing xy and yx
                    continue
                else:
                    nums[i],nums[j]=nums[j],nums[i] #swap 
        res=''.join(str(i) for i in nums) #joining list
        if int(res)==0:
            return "0"
        return res