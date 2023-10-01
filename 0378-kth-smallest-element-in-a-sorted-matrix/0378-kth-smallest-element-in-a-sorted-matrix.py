class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l=[]
        heapq.heapify(l)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if len(l)<k:
                    heapq.heappush(l,matrix[i][j]*(-1))
                else:
                    if l[0]<(matrix[i][j]*(-1)):
                        heapq.heappop(l)
                        heapq.heappush(l,matrix[i][j]*(-1))
        return heapq.heappop(l)*(-1)