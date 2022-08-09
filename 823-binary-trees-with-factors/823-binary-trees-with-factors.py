class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        arr.sort()
        
        hmap = {x: i for i, x in enumerate(arr)}
        dp = [1] * len(arr)
        
        for i, x in enumerate(arr):
            for j in range(i):
                if x % arr[j] == 0:
                    right = x / arr[j]
                    if right in hmap:
                        dp[i] += dp[j] * dp[hmap[right]]
                        dp[i] %= MOD
        return sum(dp) % MOD
                        
                        
        
        
        
        
        
        