class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = 0
        for i in range(len(nums)):
            if jump < 0:
                return False
            jump = max(nums[i], jump) - 1
        return True
            
        