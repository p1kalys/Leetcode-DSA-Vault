class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        for i in t:
            if i not in d:
                return False
            d[i]=d[i]-1
            
        for i,j in d.items():
            if j!=0:
                return False
        return True
        