class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            water = max(water, (r - l) * min(height[r], height[l]))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return water
            