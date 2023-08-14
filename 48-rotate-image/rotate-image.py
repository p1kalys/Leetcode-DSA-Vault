class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        j=0
        res=[]
        while j<len(matrix):
            r=[]
            for i in range(len(matrix)-1,-1,-1):
                r.append(matrix[i][j])
            res.append(r)
            j+=1
        matrix.clear()
        for i in res:
            matrix.append(i)