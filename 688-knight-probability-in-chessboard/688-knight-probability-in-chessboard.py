class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @lru_cache(None)
        def dfs(N, K, r, c):
            if r < 0 or r >= N or c < 0 or c >= N or K > k:
                return 0
            if K == 0:
                return 1
            
            left_up = 0.125 * dfs(N, K - 1, r - 1, c - 2)
            left_down = 0.125 * dfs(N, K - 1, r + 1, c - 2)
            down_left = 0.125 * dfs(N, K - 1, r + 2, c - 1)
            down_right = 0.125 * dfs(N, K - 1, r + 2, c + 1)
            right_down = 0.125 * dfs(N, K - 1, r + 1, c + 2)
            right_up = 0.125 * dfs(N, K - 1, r - 1, c + 2)
            up_right = 0.125 * dfs(N, K - 1, r - 2, c + 1)
            up_left = 0.125 * dfs(N, K - 1, r - 2, c - 1)
            
            return sum([left_up, left_down, down_left, down_right, right_down, right_up, up_right, up_left])
        return dfs(n, k, row, column)
        