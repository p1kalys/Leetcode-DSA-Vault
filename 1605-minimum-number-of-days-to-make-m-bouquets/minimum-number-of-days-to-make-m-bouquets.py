class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if (m * k) > len(bloomDay):
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        ans = -1
        
        def valid(day):
            bouqets = 0
            count = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= day:
                    count += 1
                else:
                    bouqets += (count // k)
                    count = 0
            bouqets += (count // k)
            if bouqets >= m:
                return True
            return False

        while (low <= high):
            mid = (low + high)//2
            if (valid(mid)):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans