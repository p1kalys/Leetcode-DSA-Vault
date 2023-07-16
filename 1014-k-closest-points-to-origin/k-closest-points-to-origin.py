class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap=[]
        for i,j in points:
            dist=(i**2)+(j**2)
            minheap.append([dist,i,j])
        heapq.heapify(minheap)
        res=[]
        while k>0:
            dist,x,y=heapq.heappop(minheap)
            res.append([x,y])
            k-=1
        return res