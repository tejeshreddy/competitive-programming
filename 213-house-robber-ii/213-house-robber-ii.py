class Solution:
    def circular_rob(self, nums):
        if len(nums) <= 2:
            return max(nums)
        
        dp = [0] * len(nums)
        
        for i in range(len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        return max(dp[-1], dp[-2])
    
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) >= 2:
            return max(self.circular_rob(nums[1:]), self.circular_rob(nums[:-1]))
        else:
            return nums[0]
        