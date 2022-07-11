class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        keys = sorted(counter.keys())
        
        dp = [0] * len(keys)
        
        for i in range(len(keys)):
            calculated_value = keys[i] * counter[keys[i]]
            
            if keys[i] - 1 not in counter:
                dp[i] = calculated_value + dp[i - 1]
            else:
                dp[i] = max(calculated_value + dp[i - 2], dp[i - 1])
        return dp[-1]
                
        
        