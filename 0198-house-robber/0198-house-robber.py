class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        
        if len(nums) <= 2:
            return max(nums)
        
        for i in range(len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        
        return max(dp[-1], dp[-2])
        