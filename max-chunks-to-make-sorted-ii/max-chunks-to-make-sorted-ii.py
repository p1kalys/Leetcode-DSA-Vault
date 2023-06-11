class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunk=0
        s1=0
        s2=0
        n=len(arr)
        cp=arr.copy()
        cp.sort()
        for i in range(n):
            s1+=cp[i]
            s2+=arr[i]
            if s1==s2:chunk+=1
        return chunk