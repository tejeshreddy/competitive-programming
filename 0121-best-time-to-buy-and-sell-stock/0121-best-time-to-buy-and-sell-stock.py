class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        result = 0
        while l < len(prices) and r < len(prices):
            if prices[l] >= prices[r]:
                l = r
                r += 1
            elif prices[l] < prices[r]:
                result = max(result, prices[r] - prices[l])
                r += 1
        return result
#         l, r = 0, len(prices) - 1
        
#         result = 0
#         while l < r:
#             if prices[r] > prices[l]:
#                 result = max(result, prices[r] - prices[l])

            
            
        