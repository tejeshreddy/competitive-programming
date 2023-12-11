class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount + 1] * (amount + 1)
        
        dp[0] = 0
        
        coins.sort()
        
        for i in range(1, amount + 1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        if dp[-1] == amount + 1:
            return -1
        return dp[-1]
            
            
            
            
        
        
        
        