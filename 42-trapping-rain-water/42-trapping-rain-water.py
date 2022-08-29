class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = []
        max_right = []
        min_value = []
        
        
        for k, v in enumerate(height):
            if k == 0:
                max_left.append(v)
            else:
                max_left.append(max(height[k - 1], max_left[-1]))
        
        for k in range(len(height) - 1, -1, -1):
            if k == len(height) - 1:
                max_right = [0] + max_right
            else:
                max_right = [max(max_right[0], height[k + 1])] + max_right
        
        for a, b in zip(max_left, max_right):
            min_value.append(min(a, b))
        
        result = 0
        
        for mv, h in zip(min_value, height):
            result += max(0, mv - h)
        return result
                
            