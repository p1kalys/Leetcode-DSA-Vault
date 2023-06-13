class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left=0
        right=n-1
        top=0
        bottom=n-1
        a=1
        matrix=[[0]*n for _ in range(n)]
        while (top<=bottom and left<=right):
            for i in range(left,right+1):
                matrix[top][i]=a
                a=a+1
            top=top+1
            for i in range(top,bottom+1):
                matrix[i][right]=a
                a+=1
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    matrix[bottom][i]=a
                    a+=1
            bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    matrix[i][left]=a
                    a+=1
            left+=1
        return matrix

