class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        length=0
        for i in sentences:
            j=i.split(" ")
            length=max(length,len(j))
        return length