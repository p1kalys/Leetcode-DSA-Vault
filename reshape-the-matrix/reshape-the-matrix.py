class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        res=[]
        ans=[]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                res.append(mat[i][j])
        if r*c!=len(res):
            return mat
        row=0
        for i in range(r):
                ans.append(res[c*i:c*i+c])
        
        return ans