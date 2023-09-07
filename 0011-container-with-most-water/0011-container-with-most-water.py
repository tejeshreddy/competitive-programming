class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = float("-inf")
        l, r = 0, len(height) - 1
        
        while l <= r:
            water = (r - l) * min(height[l], height[r])
            # print(water, l, r)
            max_water = max(water, max_water)
            
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_water
        
        