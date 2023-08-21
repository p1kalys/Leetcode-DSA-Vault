class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(n // 2, 0, -1):
            if n%i == 0:
                sub=s[:i]
                temp=""
                for j in range(1, (n // i) + 1):
                    temp+=sub
                if temp==s:
                    return True
        return False