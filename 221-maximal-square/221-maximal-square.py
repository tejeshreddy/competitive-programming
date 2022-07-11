class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        
        grid = [[0] * (cols + 1) for _ in range(rows + 1)]
        max_square = 0
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                
                if matrix[r][c] == "1":
                    
                    grid[r][c] = int(matrix[r][c]) + min(grid[r + 1][c], grid[r][c + 1], grid[r + 1][c + 1])     
                    print(r, c, grid[r][c])
                    max_square = max(max_square, grid[r][c])
        return max_square ** 2
#         max_square = 0
        
#         def bfs(r, c):
#             q = deque[(r, c)]
#             square = 1
            
            
        
        
#         for r in range(rows):
#             for c in range(cols):
#                 if matrix[r][c] == 1:
#                     bfs(r, c)
        
        
        
        
        