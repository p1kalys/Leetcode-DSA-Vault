class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res=[]
        for i in range(len(mat)):
            s = sum(mat[i])
            res.append([s,i])
        res.sort()
        output=[]
        for i in range(k):
            output.append(res[i][1])
        return output