def isValid(board,row,col,n):
    i=col
    while i>=0:
        if board[row][i]=='Q':
            return False
        i-=1
    r=row
    c=col
    while r >= 0 and c >= 0:
        if board[r][c]=='Q':
            return False
        r -= 1
        c -= 1
    i=row
    j=col
    while i<n and j>=0:
        if board[i][j]=='Q':
            return False
        i+=1
        j-=1
    return True

def Possible(board, col,ans,n):
    if col==n:
        ans.append(list(board))
        return 
    for i in range(n):
        if isValid(board,i,col,n):
            board[i] = board[i][:col] + 'Q' + board[i][col+1:]
            Possible(board, col+1,ans,n)
            board[i] = board[i][:col] + '.' + board[i][col+1:]


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        board=['.'*n for _ in range(n)]
        Possible(board,0,ans,n)
        return ans