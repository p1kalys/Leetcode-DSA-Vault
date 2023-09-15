class Solution:
    def countSubstrings(self, s: str) -> int:
        res = len(s)

        for i in range(len(s)):
            # odd case
            left, right = i-1, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

            # even case
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        
        return res