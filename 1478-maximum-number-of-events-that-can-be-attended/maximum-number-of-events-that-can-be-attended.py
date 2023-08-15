import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()

        # only for no duplication `while` after `for`
        events.append([float('inf'), float('inf')])

        result = 0
        h = []
        current_day = 0

        for start, end in events:
            while h and current_day < start:
                prev_end = heapq.heappop(h)
                if prev_end >= current_day:
                    result += 1
                    current_day += 1
            
            current_day = start
            heapq.heappush(h, end)
        
        return result