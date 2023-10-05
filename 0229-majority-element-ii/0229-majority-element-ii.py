class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1=0
        c2=0
        a1=float('-inf')
        a2=float('-inf')
        res=[]
        for i in range(len(nums)):
            if c1==0 and nums[i]!=a2:
                c1=1
                a1=nums[i]
            elif c2==0 and nums[i]!=a1:
                c2=1
                a2=nums[i]
            elif nums[i]==a1:
                c1+=1
            elif nums[i]==a2:
                c2+=1
            else:
                c1-=1
                c2-=1
        c1=0
        c2=0
        for i in range(len(nums)):
            if nums[i]==a1:
                c1+=1
            elif nums[i]==a2:
                c2+=1
        if c1>len(nums)//3:
            res.append(a1)
        if c2>len(nums)//3:
            res.append(a2)
        res.sort()
        return res