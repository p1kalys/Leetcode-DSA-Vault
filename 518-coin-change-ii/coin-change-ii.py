class Solution:
    def change(self, n: int, S: List[int]) -> int:
        size = len(S) 
        arr = [[0] * (n + 1) for _ in range(size)]
        
        for i in range(size):
            arr[i][0] = 1
        
        for i in range(0, size):
            for j in range(1, n + 1):
                t=0
                nt=0

                if j>=S[i]:  
                    t = arr[i][j - S[i]]
                if (i>0):
                    nt = arr[i - 1][j]
                arr[i][j] = t + nt
        
        return arr[size-1][n]