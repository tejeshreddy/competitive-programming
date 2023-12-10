class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_amount = 0
        
        while l < r:
            current_vol = (r - l) * min(height[l], height[r])
            max_amount = max(current_vol, max_amount)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
                
            
        return max_amount
            
        