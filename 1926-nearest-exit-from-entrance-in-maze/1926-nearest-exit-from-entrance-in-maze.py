class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = {(entrance[0], entrance[1])}
        result = float("+inf")
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        rows, cols = len(maze), len(maze[0])
        q = [(entrance, 0)]
        
        while q:
            (x, y), c = q.pop(0)
            
            if (x == rows - 1 or y == cols - 1 or x == 0 or y == 0) and [x, y] != entrance:
                result = min(result, c)
                
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and maze[nx][ny] != "+":
                    q.append(([nx, ny], c + 1))
                    visited.add((nx, ny))
        return result if result != float("+inf") else -1
        
                