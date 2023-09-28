class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i=0
        j=len(nums)-1
        while i!=j:
            mid=(i+j)//2
            if nums[mid]%2==0:
                nums[mid],nums[i]=nums[i],nums[mid]
                i+=1
            else:
                nums[mid],nums[j]=nums[j],nums[mid]
                j-=1
        return nums