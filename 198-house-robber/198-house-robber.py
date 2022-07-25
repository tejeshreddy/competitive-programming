class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return max(nums)
        dp = [0] * (len(nums))
        for i in range(len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return max(dp[-1], dp[-2])
            
            
        