class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        result = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] < 0:
                    result += cols - c
                    break
        return result
                    
        