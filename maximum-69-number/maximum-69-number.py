class Solution:
    def maximum69Number (self, num: int) -> int:
        snum=str(num)
        temp=num
        for i in range(len(snum)):
            if snum[i]=='6':
                val=int(snum[:i]+'9'+snum[i+1:])
            else:
                val=int(snum[:i]+'6'+snum[i+1:])
            temp=max(temp,val)
        return temp
