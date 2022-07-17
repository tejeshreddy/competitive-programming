class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        @lru_cache(None)
        def dfs(r, c, maxMove):
            if maxMove < 0:
                return 0
            
            if r < 0 or r == m or c < 0 or c == n:
                return 1
            
            return dfs(r + 1, c, maxMove - 1) + dfs(r - 1, c, maxMove - 1) + dfs(r, c + 1, maxMove - 1) + dfs(r, c - 1, maxMove - 1)
        
        return dfs(startRow, startColumn, maxMove) % (10 ** 9 + 7)
        
                
        