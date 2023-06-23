class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = [defaultdict(int) for _ in range(len(nums))]
        result = 0
        for i in range(len(nums)):
            for j in range(i):
                
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[j].get(diff, 1) + 1
                result = max(dp[i][diff], result)
        return result
        