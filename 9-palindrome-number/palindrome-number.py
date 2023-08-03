class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        k=list(y)
        if y==y[::-1]:
            return True
        else:
            return False