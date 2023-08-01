class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if gcd(int(str(nums[i])[0]), int(str(nums[j])[-1]))==1:
                    c+=1
        return c

    def gcd(x, y):
        count=0
        for i in range(1,max(x,y)+1):
            if x%i==0 and y%i==0:
                count+=1
        return count