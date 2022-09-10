class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        temp = 0
        for i, n in enumerate(nums):
            temp = max(temp, i + n)
            if temp == len(nums) - 1:
                return True
            if temp == i and n == 0:
                return False
        return True
            
        