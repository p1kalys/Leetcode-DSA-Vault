class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d={}
        for i in magazine:
            d[i]=d.get(i,0)+1
        for i in ransomNote:
            if i not in d:
                return False
            d[i]-=1
            if d[i]<0:
                return False
        return True