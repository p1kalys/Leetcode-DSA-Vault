class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pxor = [0] * (len(arr)+1)
        n=len(arr)
        for i in range(n):
            pxor[i]=pxor[i-1]^arr[i]
        return [pxor[j] ^ pxor[i-1] for i, j in queries]
            