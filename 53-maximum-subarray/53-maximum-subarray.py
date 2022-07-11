class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_sum = float("-inf")
        local_sum = 0
        
        for n in nums:
            local_sum += n
            global_sum = max(global_sum, local_sum)
            local_sum = max(local_sum, 0)
        return global_sum
        