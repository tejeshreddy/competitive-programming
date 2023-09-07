class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        b, s = 0, 1
        maxp = 0
        
        while s < len(prices) and b < s:
            if prices[b] > prices[s]:
                b = s
                s += 1
            else:
                maxp = max(maxp, prices[s] - prices[b])
                s += 1
        return maxp
                
                
            
            
        
        