class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        
        ans = 0
        counter = Counter()
        
        for x1, y1 in coordinates:
            for i in range(k+1):
                x2 = i ^ x1
                y2 = (k - i) ^ y1
                
                ans += counter[(x2, y2)]  # counter default value is zero, if (x2, y2) is not present it would return 0
            
            counter[(x1, y1)] += 1
        
        return ans