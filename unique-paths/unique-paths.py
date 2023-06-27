def fact(n):
    if n==1:
        return 1
    elif n==0:
        return 1
    else:
        return n*fact(n-1)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return fact(m+n-2)//(fact(m-1)*fact(n-1))