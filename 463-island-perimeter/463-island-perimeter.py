class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):    
            if (r, c) in visited:
                return 0
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == 0:
                return 1
            
            visited.add((r, c))
            return dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c)