class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        memo = {}
        
        def dp(d, t):
            if d == 0:
                return t == 0
            if t < 0:
                return 0
            if (d, t) in memo:
                return memo[d, t]
            ways = 0
            for i in range(1, k + 1):
                ways += dp(d - 1, t - i)
            memo[d, t] = ways
            return ways
        return dp(n, target) % (10 ** 9 + 7)
            