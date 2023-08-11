class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=s.lower()
        v=[]
        for i in t:
            if i.isalnum():
                v.append(i)
        i=0
        j=len(v)-1
        while i<=j:
            if v[i]!=v[j]:
                return False
            i+=1
            j-=1
        return True