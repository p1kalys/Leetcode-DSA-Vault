class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0

        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    q.appendleft((i, j, i, j))
                else:
                    grid[i][j] = math.inf

        while q:
            for _ in range(len(q)):
                i, j, i0, j0 = q.pop()
                for ii, jj in ((i-1, j), (i, j+1), (i+1, j), (i, j-1)):
                    if 0 <= ii < n and 0 <= jj < n and grid[ii][jj] == math.inf:
                        grid[ii][jj] = -(abs(ii-i0) + abs(jj-j0))
                        q.appendleft((ii, jj, i0, j0))
        
        heap = [(grid[0][0], (0, 0))]
        seen = set((0, 0))
        while heap:
            dist, cell = heappop(heap)
            i, j = cell
            if i == j == n-1:
                return -dist
            
            for ii, jj in ((i-1, j), (i, j+1), (i+1, j), (i, j-1)):
                if 0 <= ii < n and 0 <= jj < n and (ii, jj) not in seen:
                    seen.add((ii, jj))
                    heappush(heap, (max(dist, grid[ii][jj]), (ii, jj)))
                