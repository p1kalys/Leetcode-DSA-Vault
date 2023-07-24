class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)
        a=0
        b=0
        vowels=['a','e','i','o','u','A','E','I','O','U']
        for i in range(n//2):
            if s[i] in vowels:
                a+=1
            if s[n//2 +i] in vowels:
                b+=1
        if a==b:
            return True
        else:
            return False