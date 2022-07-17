class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for a in range(amount + 1):
            for c in coins:
                if a >= c and a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[-1] if dp[amount] != amount + 1 else -1
                
            
        
        
        
        
        