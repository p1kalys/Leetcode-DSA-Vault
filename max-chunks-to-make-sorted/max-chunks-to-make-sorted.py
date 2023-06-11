class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunk=0
        maxone=0
        for i,j in enumerate(arr):
            maxone=max(maxone,j)
            if maxone==i:
                chunk+=1
        return chunk