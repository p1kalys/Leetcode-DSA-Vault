class Solution:
    def gameOfLife(self, b: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(b)
        n = len(b[0])
        neighbours = [(-1,-1),(0,-1),(-1,0),(1,0),(0,1),(1,1),(1,-1),(-1,1)]

        for r in range(m):
            for c in range(n):
                count = 0

                for i , j in neighbours:
                    row = r+i
                    col = c+j
                    if row < m and row >=0 and col>= 0 and col <n:
                        count += b[r+i][c+j] % 2
                
                # the 0,1,2,3 values are put there to keep track of the previous state values 
                if (count < 2 or count >3  ) and b[r][c] == 1 :
                    b[r][c] = 1
                if count == 3 and b[r][c] == 0:
                    b[r][c] = 2
                if (count == 2 or count ==3) and b[r][c] == 1:
                    b[r][c] = 3

        for i in range(m):
            for j in range(n):
                if b[i][j] == 1:
                    b[i][j]=0
                if b[i][j] ==2:
                    b[i][j] = 1
                if b[i][j] == 3:
                    b[i][j] = 1
        