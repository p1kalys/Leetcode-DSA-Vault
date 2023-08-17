class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return mat
        
        m, n = len(mat), len(mat[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  

        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = -1
        
        distance = 1
        
        while queue:
            queue_size = len(queue)
            
            for _ in range(queue_size):
                x, y = queue.popleft()
                
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    
                    if 0 <= new_x < m and 0 <= new_y < n and mat[new_x][new_y] == -1:
                        mat[new_x][new_y] = distance
                        queue.append((new_x, new_y))
            
            distance += 1
        
        return mat