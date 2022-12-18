class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        dp[0] = 0
        
        for i in range(len(nums)):
            dp[i + 1] = max(nums[i] + dp[i - 1], dp[i])
        return max(dp[-1], dp[-2])
            
            
        