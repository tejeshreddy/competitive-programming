class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh_oranges = 0
        q = collections.deque([])
        visited = set()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        time = -1 if q else 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if (r, c) in visited:
                    continue
                
                visited.add((r, c))
                for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == 1 and (nr, nc) not in visited:
                            grid[nr][nc] = 2
                            fresh_oranges -= 1
                            q.append([nr, nc])
            time += 1
            
        return time if fresh_oranges == 0 else -1
        
                
                            
                        
                        
                        
                    
                    
                    
        
        
        