class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = [(-1, -1), (-1, 0), (-1, 1)]
        for r in range(1, rows):
            for c in range(cols):
                temp = []
                
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if nr < 0 or nr == rows or nc < 0 or nc == cols:
                        continue
                    temp.append(matrix[nr][nc])
                matrix[r][c] += min(temp)
        
        return min(matrix[-1])
        