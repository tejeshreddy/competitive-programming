class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        
        def dfs(r, c, hmap):
            if r >= rows or c >= cols:
                return 0
            if obstacleGrid[r][c] == 1:
                return 0
            if r == rows - 1 and c == cols - 1:
                return 1
            if (r, c) in hmap:
                return hmap[(r, c)]
            
            # down = dfs(r + 1, c, hmap)
            # right = dfs(r, c + 1, hmap)
            
            hmap[(r, c)] = dfs(r + 1, c, hmap) + dfs(r, c + 1, hmap)
            return hmap[(r, c)]
        
        return dfs(0, 0, {})
        
        
        