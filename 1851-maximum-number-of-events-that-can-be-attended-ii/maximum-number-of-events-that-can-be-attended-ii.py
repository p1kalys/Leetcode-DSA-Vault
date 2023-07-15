class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[0])
        n = len(events)
        
        dp = [[-1] * n for _ in range(k + 1)]
        
        def dfs(index: int, count: int) -> int:
            if count == 0 or index == n:
                return 0
            if dp[count][index] != -1:
                return dp[count][index]
            
            dp[count][index] = max(events[index][2] + dfs(binarySearch(events[index][1]), count - 1), dfs(index + 1, count))
            
            return dp[count][index]
        
        def binarySearch(target: int) -> int:
            left, right = 0, n - 1
            
            while left <= right:
                mid = left + (right - left) // 2
                if events[mid][0] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return left
        
        return dfs(0, k)