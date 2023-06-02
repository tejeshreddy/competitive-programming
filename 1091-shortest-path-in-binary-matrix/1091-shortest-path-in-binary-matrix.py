class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1:
            return -1
        
        dim = len(grid)
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        visited = set()
        queue = deque()
        
        queue.append((1, (0, 0)))
        
        while queue:
            count, (r, c) = queue.popleft()
            if r == dim - 1 and c == dim - 1:
                return count
            
            for nr, nc in directions:
                dr = r + nr
                dc = c + nc
                
                if 0 <= dr < dim and 0 <= dc < dim and grid[dr][dc] == 0 and (dr, dc) not in visited:
                    queue.append((count + 1, (dr, dc)))
                    visited.add((dr, dc))
                else:
                    continue       
        return -1
        
        
        
        