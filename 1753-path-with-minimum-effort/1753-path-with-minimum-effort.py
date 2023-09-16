
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        y_len, x_len = len(heights), len(heights[0])
        visted = [[False] * x_len for _ in range(y_len)]
        min_diff = float("inf")
        pq = [(0, 0, 0)]
        while pq:
            diff, y, x = heapq.heappop(pq)
            if y == y_len - 1 and x == x_len - 1:
                min_diff = min(min_diff, diff)
                continue
            if visted[y][x]:
                continue
            visted[y][x] = True
            curr = heights[y][x]
            # up
            if y - 1 >= 0 and not visted[y-1][x]:
                temp_y = y - 1
                temp = abs(curr - heights[temp_y][x])
                heapq.heappush(pq, (max(temp, diff), temp_y, x))
            # down
            if y + 1 < y_len and not visted[y+1][x]:
                temp_y = y + 1
                temp = abs(curr - heights[temp_y][x])
                heapq.heappush(pq, (max(temp, diff), temp_y, x))

            # left
            if x - 1 >= 0 and not visted[y][x-1]:
                temp_x = x - 1
                temp = abs(curr - heights[y][temp_x])
                heapq.heappush(pq, (max(temp, diff), y, temp_x))

            # right
            if x + 1 < x_len and not visted[y][x+1]:
                temp_x = x + 1
                temp = abs(curr - heights[y][temp_x])
                heapq.heappush(pq, (max(temp, diff), y, temp_x))


        return min_diff