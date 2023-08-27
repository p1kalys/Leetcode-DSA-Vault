class Solution:
    def isHappy(self, n: int) -> bool:
        s=[]
        while(n!=1):
            sum=0
            for i in str(n):
                sum+=(int(i)**2)
            if sum==1:
                return True
            elif sum in s:
                return False
            else:
                s.append(sum)
                n=sum
        return True