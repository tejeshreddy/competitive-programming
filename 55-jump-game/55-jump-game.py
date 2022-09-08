class Solution:
    def canJump(self, nums: List[int]) -> bool:
        temp = 0
        for i, n in enumerate(nums):
            if temp < i:
                return False
            temp = max(temp, i + n)
        return True
    
                
        