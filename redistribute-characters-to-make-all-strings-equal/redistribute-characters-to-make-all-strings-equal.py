class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        cnt = [0] * 26
        for t in words:
            for x in t:
                cnt[ord(x) - ord('a')] += 1
        n = len(words)
        for i in range(26):
            if cnt[i] % n != 0:
                return False
        return True