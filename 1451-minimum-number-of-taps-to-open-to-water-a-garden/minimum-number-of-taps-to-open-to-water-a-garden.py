class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        L = []
        for i in range(len(ranges)):
            L.append([i - ranges[i], i + ranges[i]])
        L.sort()
        i = 0
        j = 0
        count = 0
        while i < n:
            max = 0
            while j < len(L) and L[j][0] <= i:
                if L[j][1] > max:
                    max = L[j][1]
                j += 1
            if max == 0:
                return -1
            i = max
            count += 1
        return count