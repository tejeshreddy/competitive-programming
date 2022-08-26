class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or (r, c) in visited or grid[r][c] != "1":
                return
            
            grid[r][c] = "#"
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        
        island_count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    
                    island_count += 1
                    dfs(r, c)
        return island_count
                    
            