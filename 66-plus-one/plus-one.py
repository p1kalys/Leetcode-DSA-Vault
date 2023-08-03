class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''.join(str(i) for i in digits)
        s=int(s)
        s=s+1
        s=str(s)
        res=[]
        for i in range(len(s)):
            res.append(int(s[i]))
        return res