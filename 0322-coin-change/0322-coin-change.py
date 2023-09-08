class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount + 1] * amount
        print(dp)
        
        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], 1 + dp[i - c])

        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[amount]
        