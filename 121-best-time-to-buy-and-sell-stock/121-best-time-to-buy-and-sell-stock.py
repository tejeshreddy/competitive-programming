class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0
        
        if len(prices) == 1:
            return 0
        
        for r in range(len(prices)):
            if prices[r] > prices[l]:
                profit = max(profit, prices[r] - prices[l])
            else:
                l = r
        return profit
                
            
        
        