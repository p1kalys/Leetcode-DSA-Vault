class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        L=[]
        for i in range(len(ranges)):
            L.append([i-ranges[i],i+ranges[i]])
        L.sort()
        i=0
        j=0
        count=0
        while i<n:
            maxi=0
            while j<len(L) and L[j][0]<=i:
                if L[j][1]>maxi:
                    maxi=L[j][1]
                j+=1
            if maxi==0:
                return -1
            i=maxi
            count+=1 
        return count