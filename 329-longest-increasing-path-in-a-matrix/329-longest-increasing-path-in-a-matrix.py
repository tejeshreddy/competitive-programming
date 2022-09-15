class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}
        result = 0
        result = 0
        
        def dfs(r, c, prev_val):
            res = 0
            if r < 0 or c < 0 or r >= rows or c >= cols or matrix[r][c] <= prev_val:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            
            dp[(r, c)] = res
            return dp[(r, c)]
            
            
        
        for r in range(rows):
            for c in range(cols):
                
                result = max(result, dfs(r, c, -1))
        return result