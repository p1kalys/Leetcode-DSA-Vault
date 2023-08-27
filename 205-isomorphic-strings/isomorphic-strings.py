class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in d.keys() or t[i] in d.values():
                if d.get(s[i]) != t[i]:
                    return False
            else:
                d.update({s[i]: t[i]})
        return True