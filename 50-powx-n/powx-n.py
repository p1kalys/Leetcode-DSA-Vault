class Solution:
    def solve(self, x, n):
        if n == 0:
            return 1  # power of 0 is 1
        
        temp = self.myPow(x, n // 2)
        temp = temp * temp
        
        if n % 2 == 0:  # if even, return just without doing anything
            return temp
        else:
            return temp * x  # if odd, return by multiplying once more with given number
    
    def myPow(self, x, n):
        ans = self.solve(x, abs(n))
        
        if n < 0:
            return 1 / ans
        return ans