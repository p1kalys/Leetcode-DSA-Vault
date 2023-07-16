class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1=""
        s2=""
        for i in word1:
            s1+=i
        for i in word2:
            s2+=i
        if len(s1)!=len(s2):
            return False
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                return False
        return True