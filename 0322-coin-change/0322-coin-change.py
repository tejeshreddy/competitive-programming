class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("+inf")] * (amount + 1)
        dp[0] = 0
        
        for c in coins:
            for i in range(c, amount + 1):
                
                dp[i] = min(dp[i], 1 + dp[i - c])
                    
        return -1 if dp[-1] == float("+inf") else dp[-1]
        
            
            