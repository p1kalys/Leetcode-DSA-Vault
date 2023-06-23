class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        for j in range(1,numRows+1):
            ans=1
            Row=[1]
            for i in range(1,j):
                ans=ans*(j-i)
                ans=ans//i
                Row.append(ans)
            res.append(Row)
        return res