class Solution:
    def change(self, n: int, S: List[int]) -> int:
        m=len(S)
        size = m
        arr = [[0] * (n + 1) for x in range(size + 1)]
        
        for i in range(size + 1):
            arr[i][0] = 1
        
        for i in range(1, size + 1):
            for j in range(1, n + 1):
                if S[i - 1] > j:  
                    arr[i][j] = arr[i - 1][j]
                else: 
                    arr[i][j] = arr[i - 1][j] + arr[i][j - S[i - 1]]
        
        return arr[size][n]