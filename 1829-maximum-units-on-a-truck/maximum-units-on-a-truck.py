class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        count=0
        for i in boxTypes:
            if truckSize==0:
                break
            if i[0]<=truckSize:
                count+=i[0]*i[1]
                truckSize-=i[0]
            else:
                count+=truckSize*i[1]
                truckSize=0
        return count