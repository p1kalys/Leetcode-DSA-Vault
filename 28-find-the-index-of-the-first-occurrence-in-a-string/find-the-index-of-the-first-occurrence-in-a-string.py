class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0
        j=len(needle)-1
        while(j < len(haystack)):
            if (needle == haystack[i : j+1]):
                return i
            i+=1
            j+=1
        return -1