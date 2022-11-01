class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r == rows:
                return c
            new_col = c + grid[r][c]
            if new_col == -1 or new_col == cols or grid[r][new_col] != grid[r][c]:
                return -1
            return dfs(r + 1, new_col)
        
        result = []
        for c in range(cols):
            result.append(dfs(0, c))
        return result
        