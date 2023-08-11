class Solution:
    def hIndex(self, c: List[int]) -> int:
        c.sort(reverse=True)
        #if len(c)==1 and c[0]>0:
            #return 1
        #if c[-1]>=len(c):#smallest number > element number
            #return len(c)
        h = 0
        for i in range(len(c)):
            if c[i]>= i+1: #i+1 is the length from 0 to i, if c[i] < the number of 
            #elements >= c[i], then take i as the h index. Case[6,6,6,4,0],[0,0,2]
                h= i+1
        return h