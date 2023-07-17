class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i%2==0:
                d[i]=d.get(i,0)+1
        s=0
        for i in d.values():
            if s<i:
                s=i
        res_even=[]
        for i,j in d.items():
            if j==s:
                res_even.append(i)
        res_even.sort()
        if len(res_even)>=1:
            return res_even[0]
        else:
            return -1