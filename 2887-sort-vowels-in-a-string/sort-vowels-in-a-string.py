class Solution:
    def sortVowels(self, s: str) -> str:
        l=["a","A","e","E","o","O","I","i","U","u"]
        asci=[]
        for i in range(len(s)):
            if s[i] not in l:
                continue
            else:
                asci.append(ord(s[i]))
        asci.sort()
        j=0
        c=list(s)
        for i in range(len(c)):
            if c[i] in l:
                c[i]=chr(asci[j])
                j+=1
        s="".join(c)
        return s
            
        