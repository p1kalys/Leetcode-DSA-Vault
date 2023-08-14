class Solution:
    def lastRemaining(self, n: int) -> int:
        start=1
        remain=n
        left=True
        step=1
        while remain>1:
            if (left or remain%2==1):
                start+=step
            remain//=2
            step*=2
            left=not left
        return start