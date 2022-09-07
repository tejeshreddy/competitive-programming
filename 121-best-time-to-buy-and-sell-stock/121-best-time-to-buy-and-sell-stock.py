class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_purchase = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - min_purchase)
            min_purchase = min(min_purchase, prices[i])
        return max_profit