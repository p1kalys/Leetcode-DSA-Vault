import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.infiniteMin = 1
        self.heap = []
        self.inHeap = set()

    def popSmallest(self) -> int:
        if len(self.heap) == 0:
            result = self.infiniteMin
            self.infiniteMin += 1
            return result
        else:
            result = heapq.heappop(self.heap)
            self.inHeap.remove(result)
            return result
        

    def addBack(self, num: int) -> None:
        if self.infiniteMin <= num:
            return
        # mistake: forgot to check if exists
        # learning: heap allow duplicates
        # learning: read description carefully: "Adds a positive integer num back into the infinite set, if it is *not* already in the infinite set"
        if num in self.inHeap:
            return
        self.inHeap.add(num)
        heapq.heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)