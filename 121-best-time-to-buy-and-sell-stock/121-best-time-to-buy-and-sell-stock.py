class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] < l:
                l = prices[i]
            max_profit = max(max_profit, prices[i] - l)
        return max_profit
            