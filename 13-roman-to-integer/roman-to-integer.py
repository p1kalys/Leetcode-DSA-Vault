class Solution:
    def romanToInt(self, s: str) -> int:
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        ans=0
        i=0
        while i<=(len(s)-1):
            if i!=len(s)-1 and s[i]+s[i+1] in d:
                ans+=d[s[i]+s[i+1]]
                i+=2
            else:
                ans+=d[s[i]]
                i+=1
        
        return ans