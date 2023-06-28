class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        pos=heapq.nlargest(3,nums)
        neg=heapq.nsmallest(2,nums)
        return max(neg[0]*neg[1]*pos[0],pos[0]*pos[1]*pos[2])
