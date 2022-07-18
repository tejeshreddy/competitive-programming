class Solution:
    def arraySign(self, nums: List[int]) -> int:
        current = 1
        
        for i in nums:
            if i < 0:
                current *= -1
            elif i > 0:
                current *= 1
            if i == 0:
                return 0
        return current