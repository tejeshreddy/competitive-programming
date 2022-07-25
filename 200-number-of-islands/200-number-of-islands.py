class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] != "1":
                return
            grid[r][c] = "0"
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    
                    count += 1
                    dfs(r, c)
        
        return count