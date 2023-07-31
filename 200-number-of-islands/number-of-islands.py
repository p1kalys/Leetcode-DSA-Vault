class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def bfs(i, j):
            q = deque()
            q.append((i, j))
            while q:
                currRow, currCol = q.popleft()
                for dr, dc in directions:
                    r = currRow + dr
                    c = currCol + dc
                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == '1':
                        grid[r][c] = '-1'
                        q.append((r, c))
            return grid 
        count = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    bfs(i, j)
                    count += 1
        
        return count
        